from datetime import datetime
from typing import List
from src.utils.dbconn import get_conn_async, insert_conn_async
from strawberry import type


@type
class Project:
    id: int
    image: str
    cover: str
    title: str
    subtitle: str
    stack: str
    description: str
    url: str
    position: int
    date: datetime


async def get_projects(self) -> List[Project]:
    query = f'select * from portfolio.prod."PROJECTS"'
    projects = await get_conn_async(query)

    output = []
    for project in projects:
        output.append(
            Project(
                id = project['id'],
                image = project['image'],
                cover = project['cover'],
                title = project['title'],
                subtitle = project['subtitle'],
                stack = project['stack'],
                description = project['description'],
                url = project['url'],
                position = project['position'],
                date = project['date'].strftime("%y/%m/%d")
            )
        )
    return output
