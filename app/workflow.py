from llama_index.core.workflow import (
    Workflow,
    step,
    Event,
    StartEvent,
    StopEvent
)

from agents import (
    brainstorming_agent,
    Writing_plan_agent,
    Writing_agent,
    review_agent,
    doc_agent,
    query
)
import json
from llama_index.core.memory import Memory
from dotenv import load_dotenv
from uuid import uuid4
from pathlib import Path
import os
import asyncio

base_memory = Memory(token_limit=150000)
planner_memory = Memory(token_limit=150000)
writer_memory = Memory(token_limit=150000)
review_memory = Memory(token_limit=40000)
doc_memory = Memory(token_limit=100000)
APP_DIR = Path(__file__).resolve().parent


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

def latest_file(folder: str, pattern: str) -> str | None:
    base = APP_DIR / folder
    files = sorted(
        base.glob(pattern),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    return str(files[0].relative_to(APP_DIR)).replace("\\", "/") if files else None


def list_section_files(folder: str = "docsgen") -> list[str]:
    return [
        str(path.relative_to(APP_DIR)).replace("\\", "/")
        for path in sorted((APP_DIR / folder).glob("*sections-*.md"))
    ]


def build_review_message() -> str:
    plan_path = latest_file("docs", "*redaction-plan.md")
    section_paths = list_section_files()
    sections = "\n".join(f"- {path}" for path in section_paths) or "- No section files found"

    return f"""Review lightly. Do not perform a technical audit.

Use only the files listed below. Do not discover files yourself. Do not list directories. Do not read technical-findings, codebase-map, design documents, source code, tests, prompts, or config files.

Read the plan only for objective, structure, style rules, section expectations, and review checklist. Then read the section files one by one in order.

Plan:
- {plan_path or "No redaction plan found"}

Draft section files:
{sections}

Only fix wording, repetition, coherence, syntax, Markdown, transitions, and plan compliance. If a technical claim looks suspicious but the plan does not resolve it, mention it as suspicious in the summary instead of opening more files.

Keep the review report short if you create one: 150-300 words, ASCII bullets only, no decorative symbols."""

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

""" #its now a useless part
async def explorer_launch_debug(workflow_id : str): # a enlever
    response = await query(
        message=("Explore"),
        memory=explorer_memory,
        agent=exploration_agent,
        step="exploration",
        workflow_run_id=workflow_id
    )
    print(response)
    return response
"""

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




async def review_launch_debug(workflow_id : str):
    res = await query(
        message=build_review_message(),
        memory=review_memory,
        agent=review_agent,
        step="Review",
        workflow_run_id=workflow_id,
        max_iterations=20,
    )
    print(res)
    return res 

async def doc_launch_debug(workflow_id : str):
    response = await query(
        message="Go and render",
        memory=doc_memory,
        agent=doc_agent,
        step="docRender",
        workflow_run_id=workflow_id,
        max_iterations=30
    )
    print(response)
    return response

async def main():
    workflow_run_id = str(uuid4())
    print(f"\n\n Workflow ID : {workflow_run_id}\n\n")
    #await brainstorming_launch_debug(workflow_run_id)
    #await planning_launch_debug(workflow_run_id)
    #await writing_launch_debug(workflow_run_id)
    #await review_launch_debug(workflow_run_id)
    await doc_launch_debug(workflow_run_id)
    return 

asyncio.run(main())
