from datetime import datetime
from typing import List
from src.utils.dbconn import get_conn_async, insert_conn_async
from strawberry import type


@type
class Blog:
    id: int
    title: str
    subtitle: str
    description: str
    date: str
    updated: datetime
    position: int


async def get_post(self, id: int) -> Blog:
        query = f'select * from portfolio.prod."BLOG" where id = {id}'
        result = await get_conn_async(query)
        post = result[0]

        return Blog(
            id = post['id'],
            title = post['title'],
            subtitle = post['subtitle'],
            description = post['description'],
            date = post['date'],
            updated = post['updated'],
            position = post['position']
        )


async def get_blog(self) -> List[Blog]:
    query = f'select * from portfolio.prod."BLOG"'
    blog = await get_conn_async(query)
    print(blog)

    output = []
    for post in blog:
        output.append(
            Blog(
                id = post['id'],
                title = post['title'],
                subtitle = post['subtitle'],
                description = post['description'],
                date = post['date'].strftime("%y/%m/%d"),
                updated = post['updated'],
                position = post['position']
            )
        )
    return output


async def create_post(self, title: str, subtitle: str, description: str, date: datetime, updated: datetime, position: int) -> str:
        colums = "title, subtitle, description, date, updated, position"
        data = f"'{title}', '{subtitle}', '{description}', '{date}', '{updated}', {position}"
        query = f'insert into portfolio.prod."BLOG" ({colums}) values ({data});'
        await insert_conn_async(query)
        return "Post created successfully"
