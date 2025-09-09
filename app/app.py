# /app/app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller import homepage, projectlist
from config import config

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# controller
app.include_router(homepage.router)
app.include_router(projectlist.router)

"""
    login function will be build in here
"""

@app.get("/", response_class=HTMLResponse)
def root(request : Request):
    return templates.TemplateResponse("login.html", {"request" : request})

@app.post("/login", response_class=HTMLResponse)
async def login(request : Request, username : str=Form(...), password : str=Form(...)):
    user_id = config.INFO.get(username)

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
    return RedirectResponse(url=f"/projectlist/{username}", status_code=303)