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

from llama_index.core.memory import Memory
from dotenv import load_dotenv
import os
import asyncio

base_memory = Memory(token_limit=150000)

async def main():
    status = "brainstorming"
    while status == "brainstorming":
        response = await query(message="J'aimerais une documentation sur ma codebase",memory=base_memory,agent=brainstorming_agent)
        status = response.status

asyncio.run(main())
