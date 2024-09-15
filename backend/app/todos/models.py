from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from ..database import gen_uuid


class Todo(BaseModel):
    id: str = Field(default_factory=lambda: gen_uuid("todo"))
    task: str
    is_completed: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
