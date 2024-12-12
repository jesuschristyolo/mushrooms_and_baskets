from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class Freshness(str, Enum):
    very_fresh = "very_fresh"
    normal_fresh = 'normal_fresh'
    stale = 'stale'


class MushroomBase(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=200)
    edibility: bool = Field(description="Съедобность гриба")
    weight: float = Field(gt=0, le=100000,
                          description="Вес гриба должен быть больше 0 и меньше 100000 грамм")
    freshness: Freshness


class MushroomCreate(MushroomBase):
    pass


class MushroomUpdate(MushroomBase):
    pass


class Mushroom(MushroomBase):
    basket_id: Optional[int] = Field(gt=0)

    class Config:
        from_attributes = True
