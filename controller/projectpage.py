# /controller/projectpage.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import config

router = APIRouter(
    prefix="/project", 
    tags=["project"], 
    responses={404:{"description":"Not Found"}}
)
templates = Jinja2Templates(directory="templates")

# 오류 메시지 추가할 것.
@router.get("/{username}/{project_id}", response_class=HTMLResponse)
def projectpage(request:Request, username:str, project_id:str):
    user_projects = config.PROJECT.get(username)
    
    target_project = None
    for project in user_projects:
        if project["id"] == project_id:
            target_project = project
            break

    context = {
        "request":request, 
        "project":target_project, 
        "username":username, 
    }

    return templates.TemplateResponse(
        name="projectpage.html", 
        context=context
    )