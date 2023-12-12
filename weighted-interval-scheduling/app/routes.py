from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi import (
    APIRouter, 
    Request
)
from datetime import datetime

from .weightedIntervalScheduling import WeightedIntervalScheduling

class Message(BaseModel):
    message: str


server_router = APIRouter()
templates = Jinja2Templates(directory='templates')  

@server_router.get('/')
def route(request: Request, response_classe=HTMLResponse):
    return templates.TemplateResponse(
        'index.html', {'request': request}
    )

@server_router.get('/runscheduling')
def route_runscheduling(request: Request, response_model=Message):
    wis = WeightedIntervalScheduling()
    dados = request.query_params.get('tableData')
    substrings = dados.split(';')
    tasks = [sub.split(',') for sub in substrings]
    tasks.insert(0, [0, 0, 0])
    for item in tasks[1:]:
        item[0] = datetime.fromisoformat(item[0])
        item[1] = datetime.fromisoformat(item[1])
        item[2] = int(item[2])
    
    n = len(tasks)

    sorted_tasks = wis.sort_by_finish_time(tasks)
    sorted_tasks.insert(0, [0, 0, 0])

    wis.largest_compatible_indices(sorted_tasks, n-1)
    wis.iterative_compute_opt(sorted_tasks, n-1)

    wis.find_solution(n-1, sorted_tasks)

    t_weight = sum(item[2] for item in wis.scheduled_tasks)

    return {'scheduled_tasks': wis.scheduled_tasks, 't_weight': t_weight}
