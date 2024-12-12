from typing import Optional, List
from pydantic import BaseModel, Field
from app.schemas.mushroom import Mushroom


class BasketBase(BaseModel):
    id: int = Field(gt=0)
    owner_name: str = Field(max_length=200, description="Имя владельца корзины")
    capacity: float = Field(gt=0, le=1000000,
                            description="Вместительность корзины в граммах "
                                        "должна быть больше 0 и меньше 1000000 грамм")


class BasketCreate(BasketBase):
    pass


class AddMushroomToBasket(BaseModel):
    mushroom_id: int = Field(gt=0)
    basket_id: int = Field(gt=0)


class RemoveMushroomFromBasket(BaseModel):
    mushroom_id: int = Field(gt=0)


class Basket(BasketBase):
    id: int = Field(gt=0)
    mushrooms: Optional[List[Mushroom]] = Field(
        description="Список грибов, находящихся в корзине"
    )

    class Config:
        from_attributes = True
