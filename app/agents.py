from tools import (
    web_fetch,
    web_search,
    read_file,
    write_file,
    shell
)

from llama_index.core.agent import (
    FunctionAgent
)

from llama_index.llms.ollama import Ollama
import os 
from dotenv import load_dotenv

load_dotenv()

brainstorming_agent=FunctionAgent(
    
)

exploration_agent=FunctionAgent()

Writing_plan_agent=FunctionAgent()

Writing_agent=FunctionAgent() #Eux sont plusieurs,mais en sequentiel,par ce qu'ollama n'autorise pas les reqeutes en parallele

Review_agent=FunctionAgent()

doc_agent=FunctionAgent()