# /controller/projectlist.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import config

router = APIRouter(
    prefix="/projectlist", 
    tags=["projectlist"], 
    responses={404:{"discription":"Not Found"}}
)

templates = Jinja2Templates(directory="templates")

"""
    after login
    user can select project
    or make project
"""

@router.get("/{username}", response_class=HTMLResponse)
async def notionlist(request : Request, username : str):
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