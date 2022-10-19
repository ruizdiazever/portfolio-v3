from datetime import datetime
import strawberry


@strawberry.type
class Blog:
    title: str
    date: str
    description: str
    position: int


@strawberry.type
class Query:
    @strawberry.field
    def blog(self) -> Blog:
        return Blog(title="FastAPI", position=1, description="Hello", date="19/10/2022")