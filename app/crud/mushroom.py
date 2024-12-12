from app.db_engine import session_factory
from app.schemas.mushroom import Mushroom, MushroomCreate, MushroomUpdate
from fastapi import HTTPException
from app.models.mushroom import MushroomDB
import sqlalchemy
from app.crud.basket import get_or_404


class MushroomRepository:

    @staticmethod
    def get_mushroom_by_id(mushroom_id: int):
        with session_factory() as session:
            mushroom = get_or_404(session, MushroomDB, mushroom_id, 'Гриб')
            return Mushroom.model_validate(mushroom)

    @staticmethod
    def create_mushroom(new_mushroom: MushroomCreate):
        with session_factory() as session:
            try:
                new_mush = MushroomDB(
                    **{**new_mushroom.model_dump(), "freshness": new_mushroom.freshness.value}
                )
                session.add(new_mush)
                session.commit()
                return Mushroom.model_validate(new_mush)
            except sqlalchemy.exc.IntegrityError:
                raise HTTPException(
                    status_code=400,
                    detail="Гриб с этим ID уже существует"
                )

    @staticmethod
    def update_mushroom(data_mushroom: MushroomUpdate):
        with session_factory() as session:
            mushroom = get_or_404(session, MushroomDB, data_mushroom.id, 'Гриб')
            mushroom.weight = data_mushroom.weight
            mushroom.name = data_mushroom.name
            mushroom.freshness = data_mushroom.freshness.value
            mushroom.edibility = data_mushroom.edibility
            session.commit()
            return Mushroom.model_validate(mushroom)
