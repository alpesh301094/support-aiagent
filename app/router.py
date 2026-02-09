from app.chains.faq_chain import faq_chain
from app.chains.tech_chain import tech_chain
from app.chains.billing_chain import billing_chain
from app.chains.fallback_chain import fallback_chain

def route(intent: str, query: str) -> str:
    if intent == "faq":
        return faq_chain(query)
    elif intent == "technical":
        return tech_chain(query)
    elif intent == "billing":
        return billing_chain(query)
    else:
        return fallback_chain(query)
