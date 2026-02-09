from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from app.llm import get_llm

# Load FAQ file ONCE
loader = TextLoader("data/faq.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a customer support assistant.
Use ONLY the context below.

Context:
{context}

Question:
{question}

If answer not found, say:
"I don't have that information."
"""
)

def faq_chain(query: str) -> str:
    llm = get_llm()
    docs = retriever.invoke(query)

    if not docs:
        return "I don't have that information."

    context = "\n".join(d.page_content for d in docs)
    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": query
    })

    return response.content
