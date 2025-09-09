# /controller/projectpage.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/project", 
    tags=["project"], 
    responses={404:{"discription":"Not Found"}}
)
templates = Jinja2Templates(directory="templates")

"""
    homepage shows menu(function) which notion has
    1. Memo
    2. Docs
    3. 
"""

@router.get("/{project_id}", response_class=HTMLResponse)
def projectpage():
    context = {

    }
    return templates.TemplateResponse(
        name="projectlist.html", 
        context=context
    )