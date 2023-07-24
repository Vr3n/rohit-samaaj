from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("home.html", context=context)
