from pydantic import BaseModel, Field
from typing import Optional


class Error(BaseModel):
    error: str = Field(title="Описание ошибки")
    details: Optional[str] = Field(default=None, title='Дополнительные сведения об ошибке')

    class Config:
        exclude_none = True
