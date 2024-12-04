
from typing import List, Dict
from langchain_core.tools import Tool


TOOLS = {}

def load_tools(tool_names: List[str] = []) -> Dict[str, Tool]:
    """
    Load the tools with the given tool names
    """
    return {k: v for k, v in TOOLS.items() if k in tool_names}