from pydantic import BaseModel, Field

class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)

class ProjectRead(BaseModel):
    id: int
    title: str
    owner_id: int
    model_config = {"from_attributes": True}
