from llama_index.core.workflow import (
    Workflow,
    step,
    Event,
    StartEvent,
    StopEvent
)

from agents import (
    brainstorming_agent,
    exploration_agent,
    Writing_plan_agent,
    Writing_agent,
    query
)
import json
from llama_index.core.memory import Memory
from dotenv import load_dotenv
from uuid import uuid4
import os
import asyncio

base_memory = Memory(token_limit=150000)
explorer_memory = Memory(token_limit=150000)
planner_memory = Memory(token_limit=150000)
writer_memory = Memory(token_limit=150000)


def clean_json_response(content: str) -> str:
    content = content.strip()
    if content.startswith("```json"):
        content = content.removeprefix("```json").strip()
    elif content.startswith("```"):
        content = content.removeprefix("```").strip()
    if content.endswith("```"):
        content = content.removesuffix("```").strip()
    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1 and start < end:
        content = content[start:end + 1].strip()
    return content


async def brainstorming_launch_debug(workflow_id : str) :
    status = "brainstorming"
    usr_msg = "J'aimerais une documentation sur ma codebase"
    while status == "brainstorming":
        response = await query(message=usr_msg,memory=base_memory,agent=brainstorming_agent,step="brainstorming",workflow_run_id=workflow_id)
        #print(response)
        content = response.response.content
        print("\n\n DEBUG \n" + content + "\n")
        content = clean_json_response(content)
        data = json.loads(content)
        status = data['status']
        if status != "brainstorming" :
            break
        usr_msg = input("\n\n" + data['message'] + "\n")
    print("FINI")
    print(data['message']) # type: ignore
    return data['message'] # type: ignore


async def explorer_launch_debug(workflow_id : str):
    response = await query(
        message=("Explore"),
        memory=explorer_memory,
        agent=exploration_agent,
        step="exploration",
        workflow_run_id=workflow_id
    )
    print(response)
    return response

async def planning_launch_debug(workflow_id : str):
    response = await query(
        message="Your turn.Go on and follow your instructions",
        memory= planner_memory,
        agent=Writing_plan_agent,
        step="planning",
        workflow_run_id=workflow_id
    )
    print(response)
    return response

async def writing_launch_debug(workflow_id : str):
    response = await query(
        message="Commence l'ecriture",
        memory=writer_memory,
        agent=Writing_agent,
        step="Writing",
        workflow_run_id=workflow_id
    )
    print(response)
    return response


async def main():
    workflow_run_id = str(uuid4())
    print(f"\n\n Workflow ID : {workflow_run_id}\n\n")
    await brainstorming_launch_debug(workflow_run_id)
    #await explorer_launch_debug(workflow_run_id)
    #await planning_launch_debug(workflow_run_id)
    #await writing_launch_debug(workflow_run_id)
    return 

asyncio.run(main())
