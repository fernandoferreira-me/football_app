
from typing import List, Dict
from langchain_core.tools import Tool

from .self_ask_agent import get_self_ask_agent, search_team_information

def load_tools(tool_names: List[str] = []) -> Dict[str, Tool]:
    """
    Load the tools with the given tool names
    """
    TOOLS = {
        'search_team_information': search_team_information,
        "critical_search": Tool.from_function(name='Self-ask agent',
                                            func=get_self_ask_agent().invoke,
                                            description="A tool to answer complicated questions.  "
                                                        "Useful for when you need to answer questions "
                                                        "competition events like matches, or team "
                                                        "details. Input should be a question.")
    
        }
    if tool_names == []:
        return TOOLS
    return {k: v for k, v in TOOLS.items() if k in tool_names}