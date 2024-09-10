from fastnanoid import generate
import apsw

apsw.bestpractice.apply(apsw.bestpractice.recommended)

sqlite_url = f"data/test.db"

conn = apsw.Connection(sqlite_url)

# Init DB
def create_db_and_tables():
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
