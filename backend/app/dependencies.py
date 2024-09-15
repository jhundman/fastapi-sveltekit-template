from typing import Annotated
import apsw
import apsw.bestpractice
from fastapi import Header, HTTPException
from contextlib import contextmanager

apsw.bestpractice.apply(apsw.bestpractice.recommended)


@contextmanager
def get_db():
    conn = apsw.Connection("data/test.db")
    # Ephemeral Pragma
    conn.pragma("busy_timeout", 5000)  # Set busy timeout to 5000 milliseconds
    conn.pragma("cache_size", 2000)  # Cache size set to 2000 pages
    conn.pragma("temp_store", 2)  # Use memory for temporary tables (2 = memory)
    try:
        yield conn
    finally:
        conn.close()


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
