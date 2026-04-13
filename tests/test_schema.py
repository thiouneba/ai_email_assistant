from app.schemas import RoutingDecision

def test_schema():
    d = RoutingDecision(intent="request", topic="IT access", confidence=0.9, assigned_team="IT Support")
    assert d.intent == "request"
