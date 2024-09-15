from .dependencies import get_db
from .todos.models import Todo


def seed_db():
    with get_db() as conn:
        todo = Todo(task="Do homework")
        conn.execute(
            """
                INSERT OR IGNORE INTO todo (id, task, is_completed, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """,
            (
                todo.id,
                todo.task,
                int(todo.is_completed),
                todo.created_at.isoformat(),
                todo.updated_at.isoformat()
            ),
        )
