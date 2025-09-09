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

@app.post("/", response_class=HTMLResponse)
def login(request : Request):
    return templates.TemplateResponse("login.html", {"request" : request})

@app.get("/login", response_class=HTMLResponse)
def home(request : Request, username : str=Form(...), password : str=Form(...)):
    user_id = info.get(username)

    # login failed
    if not user_id or user_id.get("password") != password :
        context = {
            "resquest" : request, 
            "discription" : "Wrong ID or Password"
        }  

        return templates.TemplateResponse(
            name="login.html", 
            context=context
        )
    
    # login successed
    return templates.TemplateResponse(
        name = "login.html", 
        context=context
    )