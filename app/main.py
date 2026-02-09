from fastapi import FastAPI
from app.classifier import classify_intent
from app.router import route
from app.schemas import SupportRequest, SupportResponse

app = FastAPI(
    title="LangChain Smart Support Agent",
    version="1.0.0"
)

@app.post("/support", response_model=SupportResponse)
def support_agent(request: SupportRequest):
    intent = classify_intent(request.query)
    response = route(intent, request.query)

    return SupportResponse(
        intent=intent,
        response=response
    )
