from fastapi import FastAPI  # Depends,
from .database import create_db_and_tables
from .seed import seed_db
from .todos import todos

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(todos.router)


# Startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    seed_db()


@app.get("/")
async def root():
    return {"message": "Hello There!"}
