from fastapi import FastAPI
from app.routers.mushroom import mush_router
from app.routers.basket import basket_router
from app.crud.basket import create_tables

app = FastAPI()
app.include_router(mush_router)
app.include_router(basket_router)

create_tables()


@app.get("/")
def read_root():
    return {"message": "API запущен"}
