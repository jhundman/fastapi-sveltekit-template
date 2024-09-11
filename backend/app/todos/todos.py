from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_db
from ..database import gen_uuid
from .models import Todo
import apsw

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_db)]
)

@router.get("/")
async def get_todos():
    return Todo(task='Make Cake')

@router.get("/cake")
async def read_item(db: apsw.Connection = Depends(get_db)):
    return Todo(task='Make Cake')
