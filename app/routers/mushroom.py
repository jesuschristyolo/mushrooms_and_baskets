from fastapi import APIRouter, Depends
from app.schemas.mushroom import Mushroom, MushroomCreate, MushroomUpdate
from app.crud.mushroom import MushroomRepository

mush_router = APIRouter(
    prefix="/mushrooms",
    tags=["Взаимодействие с грибами"]
)


@mush_router.post("/create-mushroom", response_model=Mushroom)
async def create_new_mushroom(new_mushroom: MushroomCreate = Depends()):
    return MushroomRepository.create_mushroom(new_mushroom)


@mush_router.put("/update-mushroom/{mushroom_id}", response_model=Mushroom)
async def update_mushroom(mushroom_data: MushroomUpdate = Depends()):
    return MushroomRepository.update_mushroom(mushroom_data)


@mush_router.get("/get-mushroom/{mushroom_id}", response_model=Mushroom)
async def get_mushroom(mushroom_id: int):
    return MushroomRepository.get_mushroom_by_id(mushroom_id)
