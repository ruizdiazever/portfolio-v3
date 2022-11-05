from datetime import datetime
from strawberry import type

@type
class Curriculum:
    title: str
    file: str
    language: str
    date: datetime


def curriculum(self) -> Curriculum:
    return Curriculum(title="FastAPI", file="", language="ES", date=datetime.now())
