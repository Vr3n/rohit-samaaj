from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .survey.router import survey_router

app = FastAPI()

app.include_router(
    survey_router
)


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory='app/templates')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("home.html", context=context)
