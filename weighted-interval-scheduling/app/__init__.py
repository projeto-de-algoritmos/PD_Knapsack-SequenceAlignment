from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import server_router

app = FastAPI()

app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
)

app.include_router(server_router)