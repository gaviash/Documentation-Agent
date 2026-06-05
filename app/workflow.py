from llama_index.core.workflow import (
    Workflow,
    step,
    Event,
    StartEvent,
    StopEvent
)

from agents import (
    brainstorming_agent,
    query
)
import json
from llama_index.core.memory import Memory
from dotenv import load_dotenv
import os
import asyncio

base_memory = Memory(token_limit=150000)

async def main():
    status = "brainstorming"
    usr_msg = "J'aimerais une documentation sur ma codebase"
    while status == "brainstorming":
        response = await query(message=usr_msg,memory=base_memory,agent=brainstorming_agent)
        #print(response)
        content = response.response.content
        print("\n\n DEBUG \n" + content + "\n")
        data = json.loads(content)
        status = data['status']
        if status != "brainstorming" :
            break
        usr_msg = input("\n\n" + data['message'] + "\n")
    print("FINI")
    print(data['message'])
    return data['message']

asyncio.run(main())
