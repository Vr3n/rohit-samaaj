from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

survey_router = APIRouter(
    prefix='/survey',
    tags=['survey'],
)

templates = Jinja2Templates(directory='app/templates')


@survey_router.get("/", response_class=HTMLResponse)
def survey_home(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse(
        "survey/index.html",
        context=context
    )
