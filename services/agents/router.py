def handle_query(input_text: str):
    if "error" in input_text:
        return devops_agent(input_text)
    return general_agent(input_text)


def devops_agent(query):
    return f"[DevOps Agent] Investigating issue: {query}"


def general_agent(query):
    return f"[General Agent] Processing: {query}"