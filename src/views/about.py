from datetime import datetime
import strawberry


@strawberry.type
class About:
    image: str
    title: str
    content: str
    date: datetime


@strawberry.type
class Query:
    @strawberry.field
    def about(self) -> About:
        return About(image="img/about.webp", title="Ever Ruiz Diaz", content="Hello", date=datetime.now())
