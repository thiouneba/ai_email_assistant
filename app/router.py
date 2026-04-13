def route_decision(decision, retrieved_docs=None):
    if decision.confidence < 0.7:
        decision.requires_human_review = True
        return decision
    return decision
