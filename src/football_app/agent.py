from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from typing import List
from tools import load_tools

def load_agent(tool_names: List[str] = []) -> AgentExecutor:
    """
    Load the agent with the given tool names
    """
    llm = GoogleGenerativeAI(model="gemini-pro")
    prompt = hub.pull("hwchaise17/react")
    tools = load_tools(tool_names)
    agent = create_react_agent(llm, prompt, tool_names=tool_names)
    return AgentExecutor(
        agent=agent,
        tools=tools,
        handle_parsing_errors=True,
        verbose=True
    )