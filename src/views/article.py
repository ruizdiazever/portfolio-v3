from datetime import datetime
from strawberry import type

@type
class Article:
    title: str
    subtitle: str
    description: str
    date: datetime
    position: int
    url: str


def get_article(self) -> Article:
        return Article(title="FastAPI", subtitle="", description="Hello", date=datetime.now(), position=1, url="")
