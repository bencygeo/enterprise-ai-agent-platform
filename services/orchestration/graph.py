from langgraph.graph import StateGraph
from services.agents.planner_agent import planner_agent
from services.agents.executor_agent import executor_agent
from services.agents.analysis_agent import analysis_agent


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("planner", planner_agent)
    graph.add_node("executor", executor_agent)
    graph.add_node("analysis", analysis_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "analysis")

    graph.set_finish_point("analysis")

    return graph.compile()