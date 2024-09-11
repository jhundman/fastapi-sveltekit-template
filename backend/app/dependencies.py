from typing import Annotated
import apsw
from fastapi import Header, HTTPException
from contextlib import contextmanager

@contextmanager
def get_db():
    conn = apsw.Connection("data/test.db")
    try:
        yield conn
    finally:
        conn.close()


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
