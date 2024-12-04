from langchain.agents import (AgentExecutor, Tool, create_self_ask_with_search_agent)
from utils import get_search_utility


def get_self_ask_agent() -> AgentExecutor:
    """
    Get the self ask agent
    """
    # search tool
    search = get_search_utility()
    return create_self_ask_with_search_agent(
        tool=Tool(
            name='search_team_information',
            func=search.run,
            description='Useful for when you want to search '
                        'for information about a specific team or player.'
        ),
        handle_parsing_errors=True,
        verbose=True
    )