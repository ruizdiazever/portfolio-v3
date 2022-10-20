from datetime import datetime
import strawberry
from src.views.types import Curriculum


@strawberry.type
class Query:
    @strawberry.field
    def curriculum(self) -> Curriculum:
        return Curriculum(title="FastAPI", file="", language="ES", date=datetime.now())
