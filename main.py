# FASTAPI
import uvicorn
from fastapi import (Depends, FastAPI, HTTPException, Request)
from fastapi.middleware.cors import CORSMiddleware
# THIRD PACKAGES
from strawberry.asgi import GraphQL
from strawberry.schema.config import StrawberryConfig
import strawberry
# PROJECT
from src.graphql import Query, Mutation



# APP
app = FastAPI(debug=True)
origins = ['*']


# GRAPHQL
schema = strawberry.Schema(
    query=Query, 
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True)
)
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


# HOME
@app.get("/")
async def root():
    return {"message": "Hello World from my portfolio powered by FastAPI, Svelte, GraphQL, Tailwind CSS and PostgreSQL"}


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
