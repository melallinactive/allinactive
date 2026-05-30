from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/explore", response_class=HTMLResponse)
def explore(request: Request):
    return templates.TemplateResponse("explore.html", {"request": request})


@app.get("/templates/style.css")
def style():
    return FileResponse("templates/style.css", media_type="text/css")


@app.get("/favicon.ico")
def favicon():
    return FileResponse("templates/favicon.png")


@app.get("/templates/cocoon-hoodie.jpg")
def hoodie():
    return FileResponse("templates/cocoon-hoodie.jpg")