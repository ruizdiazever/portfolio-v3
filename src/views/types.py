from datetime import datetime
import strawberry


@strawberry.type
class Project:
    image: str
    cover: str
    title: str
    subtitle: datetime
    staff: int
    description: str
    url: str
    position: str
    date: datetime


@strawberry.type
class Project:
    image: str
    cover: str
    title: str
    subtitle: datetime
    staff: int
    description: str
    url: str
    position: str
    date: datetime


@strawberry.type
class Article:
    title: str
    subtitle: str
    description: str
    date: datetime
    position: int
    url: str


@strawberry.type
class Blog:
    title: str
    subtitle: str
    description: str
    date: datetime
    position: int


@strawberry.type
class Curriculum:
    title: str
    file: str
    language: str
    date: datetime
