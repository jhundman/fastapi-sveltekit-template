from fastnanoid import generate
import apsw
import apsw.bestpractice
from .dependencies import get_db

tables = {
    "todo": """
        CREATE TABLE IF NOT EXISTS todo (
            id TEXT PRIMARY KEY,
            task TEXT NOT NULL,
            is_completed INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        ) STRICT;
    """,
}


def create_db_and_tables():
    with get_db() as conn:
        print("Init Tables")
        # Persistent Pragma
        conn.pragma("journal_mode", "wal")  # WAL mode for better write performance
        conn.pragma("synchronous", "normal")  # Normal synchronous mode
        conn.pragma("foreign_keys", True)  # Enable foreign keys

        for table_name, create_table_sql in tables.items():
            conn.execute(create_table_sql)


# Generate Nano UUIDs
alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
prefixes = {"todo": "td"}


def gen_uuid(prefix: str) -> str:
    if prefix not in prefixes:
        raise ValueError(f"Invalid prefix: {prefix}")
    return prefixes[prefix] + "_" + generate(alphabet, size=16)


def row_tracer(cursor: apsw.Cursor, row):
    """
    Called with each row of results before they are handed off.
    Used to map to dict for Pydantic type parsing.
    """
    return (
        {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
        if row
        else None
    )
