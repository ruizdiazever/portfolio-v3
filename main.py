import uvicorn
from fastapi import (Depends, FastAPI, HTTPException, Request)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=True)
origins = ['*']


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
async def root():
    return {"name": "Ever"}


app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
