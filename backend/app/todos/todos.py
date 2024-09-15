from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import get_db
from .models import Todo
from datetime import datetime
from ..database import row_tracer
import apsw

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_db)],
)


@router.get("/", response_model=list[Todo] | None)
async def get_todos(db: apsw.Connection = Depends(get_db)):
    with db as conn:
        cursor = conn.cursor()
        cursor.row_trace = row_tracer
        rows = cursor.execute("SELECT * FROM todo;")
        return [Todo(**row) for row in rows]


@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str, db: apsw.Connection = Depends(get_db)):
    with db as conn:
        cursor = conn.cursor()
        cursor.row_trace = row_tracer
        cursor.execute("SELECT * FROM todo WHERE id = ?;", (todo_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Todo not found")
        return Todo(**row)


@router.post("/", status_code=201, response_model=Todo)
async def create_todo(todo: Todo, db: apsw.Connection = Depends(get_db)):
    with db as conn:
        conn.execute(
            "INSERT INTO todo VALUES (?,?,?,?,?);",
            (
                todo.id,
                todo.task,
                todo.is_completed,
                todo.created_at.isoformat(),
                todo.updated_at.isoformat(),
            ),
        )
    return todo


@router.put("/{todo_id}")
async def update_todo(todo_id: str, todo: Todo, db: apsw.Connection = Depends(get_db)):
    updated_at = datetime.utcnow().isoformat()
    with db as conn:
        cursor = conn.cursor()
        cursor.row_trace = row_tracer
        cursor.execute(
            "UPDATE todo SET task = ?, is_completed = ?, updated_at = ? WHERE id = ? RETURNING *;",
            (todo.task, todo.is_completed, updated_at, todo_id),
        )
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Todo not found")
        return Todo(**row)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str, db: apsw.Connection = Depends(get_db)):
    with db as conn:
        cursor = conn.cursor()
        cursor.row_trace = row_tracer
        cursor.execute(
            "DELETE FROM todo WHERE id = ? RETURNING *;",
            (todo_id,),
        )
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Todo not found")
        return
