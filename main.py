from strawberry.asgi import GraphQL
import strawberry
import uvicorn
from fastapi import (Depends, FastAPI, HTTPException, Request)
from fastapi.middleware.cors import CORSMiddleware
from src.blog import Query


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
    uvicorn.run(app, host="0.0.0.0", port=8000)
