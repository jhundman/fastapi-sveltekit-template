from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header
from ..database import gen_uuid
from .models import Todo


router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)


@router.get("/cake")
async def read_item():
    return Todo(task='Make Cake')
