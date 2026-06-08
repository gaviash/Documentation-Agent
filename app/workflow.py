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


async def brainstorming_launch_debug(workflow_id : str) :
    status = "brainstorming"
    usr_msg = "J'aimerais une documentation sur ma codebase"
    while status == "brainstorming":
        response = await query(message=usr_msg,memory=base_memory,agent=brainstorming_agent,step="brainstorming",workflow_run_id=workflow_id)
        #print(response)
        content = response.response.content
        print("\n\n DEBUG \n" + content + "\n")
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


async def main():
    workflow_run_id = str(uuid4())
    await brainstorming_launch_debug(workflow_run_id)
    return 

asyncio.run(main())
