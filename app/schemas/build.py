from pydantic import BaseModel


class Build(BaseModel):
    build: str