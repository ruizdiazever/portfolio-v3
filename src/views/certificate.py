from datetime import datetime
import strawberry


@strawberry.type
class Certificate:
    title: str
    image: str
    url: str
    position: int


@strawberry.type
class Query:
    @strawberry.field
    def certificate(self) -> Certificate:
        return Certificate(title="FastAPI", image="img/certificate.webp", position=1, url="Hello")
