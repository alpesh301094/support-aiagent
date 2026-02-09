from app.llm import get_llm

def billing_chain(query: str) -> str:
    llm = get_llm()
    return llm.invoke(
        f"Respond professionally to this billing issue:\n{query}"
    ).content
