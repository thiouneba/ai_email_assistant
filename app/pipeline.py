from .schemas import RoutingDecision
from .router import route_decision


def classify_email(email_text: str, context_text: str | None = None) -> RoutingDecision:
    lowered = email_text.lower()
    intent = "request" if any(w in lowered for w in ["need", "please", "can you", "could you", "request"]) else "other"
    topic = "IT access" if any(w in lowered for w in ["access", "login", "permission", "dashboard"]) else "general inquiry"
    subtopic = "permissions" if "access" in lowered else None
    decision = RoutingDecision(
        intent=intent,
        topic=topic,
        subtopic=subtopic,
        confidence=0.60 if context_text is None else 0.78,
        assigned_team="IT Support" if topic == "IT access" else "General Operations",
        assigned_expert=None,
        reasons=["Basic keyword match"],
        requires_human_review=False,
    )
    return route_decision(decision)
