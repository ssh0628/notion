# /app/app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller import projectlist, projectpage
from config import config

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# controller
app.include_router(projectpage.router)
app.include_router(projectlist.router)

"""
    login function will be build in here
"""

# Root
@app.get("/", response_class=HTMLResponse)
def root(request : Request, message : str | None=None):
    context = {
        "request" : request, 
        "message" : message, 
    }
    return templates.TemplateResponse(
        name = "login.html", 
        context=context
    )

# Log In
@app.post("/login", response_class=HTMLResponse)
async def login(request : Request, username : str=Form(...), password : str=Form(...)):
    user_id = config.INFO.get(username)

    # login failed
    if not user_id or user_id.get("password") != password :
        context = {
            "request" : request, 
            "message" : "유효하지 않는 ID 또는 비밀번호 입니다."
        }  

        return templates.TemplateResponse(
            name="login.html", 
            context=context
        )
    
    # login successed
    return RedirectResponse(url=f"/projectlist/{username}", status_code=303)

# Sign Up
@app.get("/signup", response_class=HTMLResponse)
async def signup(request : Request):

    context={
        "request" : request
    }

    return templates.TemplateResponse(
        name="signup.html", 
        context=context
    )

@app.post("/signup")
async def signingup(request : Request, username : str=Form(...), password : str=Form(...), confirm_password : str=Form(...)):
    if password != confirm_password:
        context = {
            "request" : request, 
            "message" : "비밀번호가 일치하지 않습니다.", 
            "success" : False, 
        }
        return templates.TemplateResponse(
            name="signup.html", 
            context=context
        )
    
    if username in config.INFO:
        context = {
            "request" : request, 
            "message" : "사용중인 사용자 아이디입니다.", 
            "success" : False, 
        }

        return templates.TemplateResponse(
            name="signup.html", 
            context=context
        )

    config.INFO[username] = {"password":password}

    success_message = "회원가입이 완료되었습니다. 로그인 해주세요."

    return RedirectResponse(url=f"/?message={success_message}", status_code=303)