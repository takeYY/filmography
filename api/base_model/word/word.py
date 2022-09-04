from pydantic import BaseModel


class Word(BaseModel):
    target: str
