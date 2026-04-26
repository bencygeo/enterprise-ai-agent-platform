import os
from langchain_openai import ChatOpenAI

def get_llm():
    """Initialize ChatOpenAI with API key from environment variable."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it before running the application."
        )
    return ChatOpenAI(openai_api_key=api_key)

def planner_agent(state):
    query = state["input"]
    
    llm = get_llm()

    prompt = f"""
    You are a DevOps planner.

    Break this issue into investigation steps:
    Issue: {query}
    """

    plan = llm.invoke(prompt)

    return {"plan": plan}