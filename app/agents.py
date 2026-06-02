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