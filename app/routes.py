from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi import (
    APIRouter, 
    Request
)

class Message(BaseModel):
    message: str


server_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@server_router.get('/')
def route(request: Request, response_classe=HTMLResponse):
    return templates.TemplateResponse(
        'index.html', {'request': request}
    )