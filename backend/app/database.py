from fastnanoid import generate
import apsw
import apsw.bestpractice
from .dependencies import get_db

apsw.bestpractice.apply(apsw.bestpractice.recommended)

def create_db_and_tables():
    with get_db() as conn:  # This should work now since get_db is synchronous
        conn.execute("CREATE TABLE IF NOT EXISTS point(x,y,z)")
        conn.execute("insert into point values(1, 2, 3)")
        for row in conn.execute("select * from point"):
            print(row)


# Generate Nano UUIDs
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
prefixes = {
    "todo": "td"
}

def gen_uuid(prefix: str) -> str:
    if prefix not in prefixes:
        raise ValueError(f"Invalid prefix: {prefix}")
    return prefixes[prefix] + "_" + generate(alphabet, size=16)
