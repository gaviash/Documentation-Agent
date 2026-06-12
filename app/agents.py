from tools import (
    web_fetch,
    web_search,
    read_file,
    write_file,
    edit_file,
    shell,
    ask_user
)

from llama_index.core.agent import (
    FunctionAgent,
)

from llama_index.core.agent.workflow import (
    AgentStream,
    ToolCall,
    ToolCallResult
)

from llama_index.llms.ollama import Ollama 
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from langfuse import get_client,propagate_attributes
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
LlamaIndexInstrumentor().instrument()
langfuse = get_client()


def load_prompt(filenames : list[str]) -> str:
    p = Path(__file__).resolve().parent.parent / str(os.getenv("PROMPTS_DIR"))
    parts = [(p / "general_prompt.md").read_text(encoding="utf-8").strip()]
    for file in filenames :
        path = p / file
        parts.append(path.read_text(encoding="utf-8").strip())
    return "\n\n".join(part for part in parts if part)

first_model = Ollama(
    model=str(os.getenv("OLLAMA_MODEL")),
    temperature=0.0,
    context_window=262144,
    request_timeout=150.0,
    base_url="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
    }
)

review_model = Ollama(
    model=str(os.getenv("REVIEW_MODEL")),
    temperature=0.0,
    context_window=262000,
    request_timeout=150.0,
    base_url="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
    }
)

"""
groq_model = Groq(
    model=os.getenv("GROQ_MODEL"), # type: ignore
    api_key=os.getenv("GROQ_API_KEY")
)
"""

"""
nvidia_model=NVIDIA(
    model=str(os.getenv("NVIDIA_MODEL")),
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)
"""

brainstorming_agent=FunctionAgent(
    name="BrainstormingAgent",
    llm=first_model,
    system_prompt=load_prompt(["brainstorming_agent.txt","brainstorming.md"]),
    tools=[web_fetch,web_search,read_file,write_file,shell],
    timeout=260.0
    
    
)

"""
exploration_agent=FunctionAgent( #a enlever
    name="ExplorationAgent",
    llm=first_model,
    system_prompt=load_prompt(["codebase-exploration.md"]),
    tools=[read_file,write_file,shell],
    timeout=200
)
"""

Writing_plan_agent=FunctionAgent(
    name="WritingPlanAgent",
    llm=first_model,
    system_prompt=load_prompt(["redac-planning.md"]),
    tools=[read_file,write_file,shell],
    timeout=200
)


Writing_agent=FunctionAgent(
    name="WritingAgent",
    llm=first_model,
    system_prompt=load_prompt(["redac-writing.md"]),
    tools=[write_file,read_file,shell,edit_file],
    timeout=200    
)

#Eux sont plusieurs,mais en sequentiel,par ce qu'ollama n'autorise pas les reqeutes en parallele

review_agent=FunctionAgent(
    name="reviewAgent",
    llm=review_model,
    system_prompt=load_prompt(["redac-review.md"]),
    tools=[read_file,edit_file,write_file],
    timeout=250
)

doc_agent=FunctionAgent(
    name="DocAgent",
    llm=first_model,
    system_prompt=load_prompt(["doc-agent.md"]),
    tools=[write_file,read_file,edit_file,shell],
    timeout=100.0
)


async def query(message,memory,agent : FunctionAgent,step : str,workflow_run_id : str,max_iterations : int = 50):
    metadata={
                "workflow_run_id": workflow_run_id,
                "step": step,
                "agent": agent.name,
    }
    with langfuse.start_as_current_observation(
        name=step,
        as_type="agent",
        input=message,
        metadata=metadata
    ) as observation :
        
        with propagate_attributes(
            session_id=workflow_run_id,
            trace_name=f"{step}:{workflow_run_id[:8]}",
            tags=["documentation-workflow", step],
            metadata=metadata,
        ):
    
            handler = agent.run(user_msg=message,memory=memory,max_iterations=max_iterations)
            async for event in handler.stream_events():
                if isinstance(event, AgentStream):
                    if event.delta:
                        continue
                elif isinstance(event, ToolCall):
                    print("\n[TOOL CALL]")
                    print(f"Tool : {event.tool_name} \n")
                    print(f"Arguments : {event.tool_kwargs}")
                elif isinstance(event,ToolCallResult):
                    print("\n[TOOL RESULT]")
                    print(f"Result : {str(event.tool_output)[:1000]}")
        
            response = await handler
        
        observation.update(output=str(response))
    langfuse.flush()
    return response
