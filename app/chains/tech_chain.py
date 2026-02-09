from app.llm import get_llm

def tech_chain(query: str) -> str:
    llm = get_llm()
    return llm.invoke(
        f"Provide troubleshooting steps for:\n{query}"
    ).content
