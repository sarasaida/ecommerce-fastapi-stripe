from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from src import app, schemas

router = APIRouter(
    tags = ['User Interface']
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))

@router.get("/", status_code=status.HTTP_200_OK)
def index(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request" : request})


@router.get("/products", status_code=status.HTTP_200_OK)
def products_index(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("ecommerce/index.html", {"request" : request})
