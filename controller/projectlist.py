# /controller/notionList.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/projectlist", 
    tag=["projectlist"], 
    responses={404:{"discription":"Not Found"}}
)
templates = Jinja2Templates(directory="templates")

"""
    after login
    user can select project
    or make project
"""

@router.post("", responses_class=HTMLResponse)
def notionlist(request : Request):
    context = {

    }
    return templates.TemplateResponse(
        name="projectlist.html", 
        context=context
    )