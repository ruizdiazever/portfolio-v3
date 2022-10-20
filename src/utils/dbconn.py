import asyncio
import psycopg
from src.settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER


CONN_INFO = f"dbname={DB_DATABASE} user={DB_USER} port={DB_PORT} host={DB_HOST} password={DB_PASSWORD}"
CONN_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?sslmode=require"


async def get_conn_async(query=str):
    async with await psycopg.AsyncConnection.connect(conninfo=CONN_INFO) as async_conn:
        async with async_conn.cursor() as async_cursor:
            await async_cursor.execute(query)
            async for record in async_cursor:
                print(record)


async def get_conn_async_v2(query=str):
    async with await psycopg.AsyncConnection.connect(conninfo=CONN_INFO) as async_conn:
        async with async_conn.cursor() as async_cursor:
            records = await async_cursor.execute(query)
            column_names = list(map(lambda x: x.lower(), [
                d[0] for d in records.description]))
            rows = list(await records.fetchall())
            output = [dict(zip(column_names, row)) for row in rows]
            return output


def get_conn():
    connection = psycopg.connect(conninfo=CONN_INFO)
    return connection


def get_data_db(query=str):
    connection = get_conn()
    cursor = connection.cursor()
    cursor.execute(query)
    column_names = list(map(lambda x: x.lower(), [
        d[0] for d in cursor.description]))
    rows = list(cursor.fetchall())
    output = [dict(zip(column_names, row)) for row in rows]
    return output
