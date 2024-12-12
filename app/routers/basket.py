from fastapi import APIRouter, Depends
from app.schemas.basket import Basket, BasketCreate, AddMushroomToBasket, RemoveMushroomFromBasket
from app.crud.basket import BasketRepository

basket_router = APIRouter(
    prefix="/baskets",
    tags=["Взаимодействие с корзинами"]
)


@basket_router.post('/create-basket', response_model=Basket)
async def create_new_basket(new_basket: BasketCreate = Depends()):
    return BasketRepository.create_new_basket(new_basket)


@basket_router.post('/put-mushroom', response_model=Basket)
async def put_mushroom_in_basket(data: AddMushroomToBasket = Depends()):
    return BasketRepository.add_mushroom_in_basket(data)


@basket_router.delete('/delete-mushroom', response_model=Basket)
async def delete_mushroom_from_basket(data: RemoveMushroomFromBasket = Depends()):
    return BasketRepository.delete_mushroom_from_basket(data)


@basket_router.get('/get-basket', response_model=Basket)
async def get_basket(basket_id: int):
    return BasketRepository.get_basket(basket_id)
