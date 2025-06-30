from pydantic import BaseModel, Field


class Error(BaseModel):
    error: str = Field(title="Описание ошибки")
