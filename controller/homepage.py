# /controller/homepage.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/homepage", 
    tag=["homepage"], 
    responses={404:{"discription":"Not Found"}}
)
templates = Jinja2Templates(directory="templates")

"""
    homepage shows menu(function) which notion has
    1. Memo
    2. Docs
    3. 
"""

@router.get("")
def homepage():
    context = {

    }
    return templates.TemplateResponse(
        name="projectlist.html", 
        context=context
    )