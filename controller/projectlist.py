# /controller/projectlist.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import config
from pydantic import BaseModel 
from datetime import datetime

router = APIRouter(
    prefix="/projectlist", 
    tags=["projectlist"], 
    responses={404:{"discription":"Not Found"}}
)

class ProjectCreate(BaseModel):
    name: str

templates = Jinja2Templates(directory="templates")

"""
    after login
    user can select project
    or make project
"""

@router.get("/{username}", response_class=HTMLResponse)
async def projectlist(request : Request, username : str):
    projects = config.PROJECT.get(username, [])

    context = {
        "request" : request, 
        "username" : username, 
        "projects" : projects
    }

    return templates.TemplateResponse(
        name="projectlist.html", 
        context=context
    )

@router.post("/{username}")
async def makeproject(request : Request, username : str, project_data : ProjectCreate):
    project_count = len(config.PROJECT.get(username, []))

    new_project = {
        "id" : f"project{project_count + 1}",
        "name" : project_data.name, 
        "create_date" : datetime.now().strftime("%Y-%-m-%d"), 
    }

    if username in config.PROJECT:
        config.PROJECT[username].append(new_project)
    else:
        config.PROJECT[username] = [new_project]

    return new_project