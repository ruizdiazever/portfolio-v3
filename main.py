# FASTAPI
import uvicorn
from fastapi import (Depends, FastAPI, HTTPException, Request)
from fastapi.middleware.cors import CORSMiddleware
# THIRD PACKAGES
from strawberry.asgi import GraphQL
import strawberry
# PROJECT
from src.views.blog import Query
from src.utils.dbconn import get_conn_async, get_data_db, get_conn_async_v2


# APP
app = FastAPI(debug=True)
origins = ['*']


# GRAPHQL
schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


# HOME
@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI, Svelte, GraphQL and RedisDB"}


# TEST DB
@app.get("/db")
def db_test():
    query = 'select name from berli.prod."USERS"'
    data = get_data_db(query)
    return {"data": data}


# TEST DB ASYNC
@app.get("/db/async")
async def db_async_test():
    query = 'select name from berli.prod."USERS"'
    await get_conn_async(query)
    return {"message": "Test DB Success, see terminal!"}


# TEST 2 DB ASYNC
@app.get("/db/async/v2")
async def db_async_v2_test():
    query = 'select name from berli.prod."USERS"'
    data = await get_conn_async_v2(query)
    return {"message": data}


# CORS
app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# INIT
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5005)
