from app.llm import get_llm

def fallback_chain(query: str) -> str:
    llm = get_llm()
    return llm.invoke(
        f"Ask the user to clarify:\n{query}"
    ).content
