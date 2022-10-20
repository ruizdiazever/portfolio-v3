from datetime import datetime
import strawberry
from src.views.types import Blog


@strawberry.type
class Query:
    @strawberry.field
    def blog(self) -> Blog:
        return Blog(title="FastAPI", subtitle="", position=1, description="Hello", date=datetime.now())
