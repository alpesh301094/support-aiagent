from langchain_core.prompts import PromptTemplate
from app.llm import get_llm

prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are a customer support intent classifier.

Classify the query into ONE of:
- faq
- technical
- billing
- unknown

Query:
{query}

Respond with only one word.
"""
)

def classify_intent(query: str) -> str:
    llm = get_llm()
    chain = prompt | llm
    result = chain.invoke({"query": query})
    return result.content.strip().lower()