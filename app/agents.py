from tools import (
    web_fetch,
    web_search,
    read_file,
    write_file,
    shell,
    ask_user
)

from llama_index.core.agent import (
    FunctionAgent
)

from llama_index.core.agent.workflow import (
    AgentStream,
    ToolCall,
    ToolCallResult
)

from llama_index.llms.ollama import Ollama 
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

def load_prompt(filenames : list[str]) -> str:
    p = Path(__file__).resolve().parent.parent / str(os.getenv("PROMPTS_DIR"))
    parts = [(p / "general_prompt.md").read_text(encoding="utf-8").strip()]
    for file in filenames :
        path = p / file
        parts.append(path.read_text(encoding="utf-8").strip())
    return "\n\n".join(part for part in parts if part)

first_model = Ollama(
    model=str(os.getenv("OLLAMA_MODEL")),
    temperature=0.1,
    context_window=262144,
    request_timeout=100.0,
    base_url="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
    }
)

brainstorming_agent=FunctionAgent(
    name="BrainstormingAgent",
    llm=first_model,
    system_prompt=load_prompt(["brainstorming_agent.txt","brainstorming.md"]),
    tools=[web_fetch,web_search,read_file,write_file,shell],
    timeout=100.0
    
    
)



"""
exploration_agent=FunctionAgent()

Writing_plan_agent=FunctionAgent()

Writing_agent=FunctionAgent() #Eux sont plusieurs,mais en sequentiel,par ce qu'ollama n'autorise pas les reqeutes en parallele

Review_agent=FunctionAgent()

doc_agent=FunctionAgent()
"""

async def query(message,memory,agent : FunctionAgent):
    handler = agent.run(user_msg=message,memory=memory,max_iterations=30)
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
    return response
