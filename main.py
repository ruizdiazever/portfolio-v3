import os
from os.path import join, dirname
# FASTAPI
import uvicorn
from fastapi import Query as QueryFastAPI
from fastapi import (Depends, FastAPI, HTTPException, Request)
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
# THIRD PACKAGES
from strawberry.asgi import GraphQL
from strawberry.schema.config import StrawberryConfig
import strawberry
# PROJECT
from src.graphql import Query, Mutation
from src.egg import snake


# APP
app = FastAPI(
        debug=True,
        title="Portfolio v3",
        description="Portfolio web v3 maked with Python 3.11, FastAPI, GraphQL, Svelte, Tailwind CSS and PostgreSQL",
        version="0.0.1",
        docs_url="/docs",
        redoc_url="/redoc"
    )
app.mount("/home", StaticFiles(directory="frontend/build", html=True), name="home")
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
    return RedirectResponse(url='home')


@app.get("/download/cv/{language}")
async def file_cv(language: str = QueryFastAPI(default="en", min_length=2, max_length=2)):
    absolute_path = join(dirname(__file__))
    file_location = f"{absolute_path}/src/files/cv_{language}.pdf"
    return FileResponse(file_location, media_type='application/octet-stream', filename='cv.pdf')


@app.get("/info")
async def info():
    return {
        "message": "Hello from my web portfolio v3 powered by FastAPI, Svelte, GraphQL, Tailwind CSS and PostgreSQL",
        "cores": os.cpu_count()
    }


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
