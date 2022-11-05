from datetime import datetime
from strawberry import type


@type
class Certificate:
    title: str
    image: str
    url: str
    position: int


def certificate(self) -> Certificate:
    return Certificate(title="FastAPI", image="img/certificate.webp", position=1, url="Hello")
