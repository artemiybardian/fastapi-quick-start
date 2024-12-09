from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    name: str = Field(max_length=64)
    email: str = Field(max_length=64)
