from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..database import gen_uuid


class Todo(BaseModel):
    id: str = Field(default_factory=lambda: gen_uuid('todo'))
    task: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
