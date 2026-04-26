def executor_agent(state):
    plan = state["plan"]

    return {"execution": f"Executing steps: {plan}"}