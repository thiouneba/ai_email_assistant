from pydantic import BaseModel, Field
from typing import Literal, Optional, List

class EmailInput(BaseModel):
    subject: str = ""
    body: str
    sender: Optional[str] = None

class RoutingDecision(BaseModel):
    intent: Literal["request", "suggestion", "claim", "question", "complaint", "escalation", "other"]
    topic: str = Field(..., description="Main business topic")
    subtopic: Optional[str] = Field(default=None, description="More specific issue")
    confidence: float = Field(..., ge=0.0, le=1.0)
    assigned_team: str
    assigned_expert: Optional[str] = None
    reasons: List[str] = Field(default_factory=list)
    requires_human_review: bool = False
