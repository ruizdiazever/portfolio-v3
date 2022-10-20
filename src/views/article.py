from datetime import datetime
import strawberry
from src.views.types import Article


@strawberry.type
class Query:
    @strawberry.field
    def article(self) -> Article:
        return Article(title="FastAPI", subtitle="", description="Hello", date=datetime.now(), position=1, url="")
