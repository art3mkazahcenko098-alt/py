from datetime import datetime
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=2000)

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=2000)
    is_done: bool | None = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool
    created_at: datetime
    project_id: int
    model_config = {"from_attributes": True}
