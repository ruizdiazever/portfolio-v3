from datetime import datetime
import strawberry
from src.views.types import Project


@strawberry.type
class Query:
    @strawberry.field
    def project(self) -> Project:
        return Project(image="", cover="", title=1, subtitle="Hello", staff="Python", description="", url="", position="", date=datetime.now())
