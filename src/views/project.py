from datetime import datetime
from strawberry import type

@type
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


def project(self) -> Project:
    return Project(image="", cover="", title=1, subtitle="Hello", staff="Python", description="", url="", position="", date=datetime.now())
