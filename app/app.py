# /app/app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controller import homepage, projectlist

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# controller
app.include_router(homepage.router)
app.include_router(projectlist.router)

"""
    login function will be build in here
"""

# test user info
info = {
    # user_id : {password:password}
    "asd123" : {"password":"asd123"}, 
}

@app.get("/", response_class=HTMLResponse)
def home(request : Request, userid : str=Form(...), password : str=Form(...)):
    
    context = {
        "resquest" : request, 
        "name" : "Root Page", 
        "discription" : "This is Root Page."
    }
    return templates.TemplateResponse(
        name = "login.html", 
        context=context
    )

@app.post("/login", response_class=HTMLResponse)
def login(request : Request):
    return