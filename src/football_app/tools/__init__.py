
from typing import List, Dict
from langchain_core.tools import Tool

from utils import get_search_utility
from self_ask_agent import get_self_ask_agent

TOOLS = {
    'search_team_information': Tool( name='Search information about team',
                                     func=get_search_utility().run,
                                     description='Useful for when you want to search '
                                                 'for information about a specific team.'),
    "critical_search": Tool.from_function(name='Self-ask agent',
                                          func=get_self_ask_agent().invoke,
                                          description="A tool to answer complicated questions.  "
                                                      "Useful for when you need to answer questions "
                                                      "competition events like matches, or team "
                                                      "details. Input should be a question.")
 
    }

def load_tools(tool_names: List[str] = []) -> Dict[str, Tool]:
    """
    Load the tools with the given tool names
    """
    return {k: v for k, v in TOOLS.items() if k in tool_names}