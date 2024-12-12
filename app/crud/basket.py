from app.db_engine import sync_engine, Base, session_factory
from app.schemas.basket import BasketCreate, Basket, AddMushroomToBasket, RemoveMushroomFromBasket
from fastapi import HTTPException
from app.models.basket import BasketDB
from app.models.mushroom import MushroomDB
import sqlalchemy


def create_tables():
    Base.metadata.create_all(sync_engine)


def get_or_404(session, model, object_id, object_name="Объект"):
    instance = session.query(model).filter_by(id=object_id).first()
    if object_id < 0:
        raise HTTPException(
            status_code=400, detail=f"id должен быть положительным числом"
        )
    if not instance:
        raise HTTPException(
            status_code=404, detail=f"{object_name} под {object_id} id не найден"
        )
    return instance


class BasketRepository:

    @staticmethod
    def create_new_basket(new_basket: BasketCreate):
        with session_factory() as session:
            try:
                new_basket = BasketDB(
                    **{**new_basket.model_dump()}
                )
                session.add(new_basket)
                session.commit()
                return Basket.model_validate(new_basket)
            except sqlalchemy.exc.IntegrityError:
                raise HTTPException(
                    status_code=400,
                    detail="Корзина с этим ID уже существует"
                )

    @staticmethod
    def add_mushroom_in_basket(data: AddMushroomToBasket):
        with session_factory() as session:
            basket = get_or_404(session, BasketDB, data.basket_id, 'Корзинка')
            mushroom = get_or_404(session, MushroomDB, data.mushroom_id, 'Гриб')

            if mushroom.basket:
                if mushroom.basket == basket:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Гриб с {data.mushroom_id} id уже находится в этой корзине."
                    )
                else:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Гриб с {data.mushroom_id} id в данный момент находится в другой корзине."
                    )

            total_weight = sum(mushroom.weight for mushroom in basket.mushrooms) + mushroom.weight
            if total_weight > basket.capacity:
                raise HTTPException(
                    status_code=400,
                    detail=f"Вы не можете добавить гриб весом в {mushroom.weight} в корзину."
                           f" Максимальная грузоподъёмность корзины - {basket.capacity}."
                           f" После добавления гриба корзина будет заполнена на {total_weight} грамм",
                )

            basket.mushrooms.append(mushroom)
            session.add(basket)
            session.commit()
            return Basket.model_validate(basket)

    @staticmethod
    def delete_mushroom_from_basket(data: RemoveMushroomFromBasket):
        with session_factory() as session:
            mushroom = get_or_404(session, MushroomDB, data.mushroom_id, 'Гриб')
            if not mushroom.basket:
                raise HTTPException(
                    status_code=400,
                    detail=f"Гриб с {data.mushroom_id} id не находится в корзине"
                )
            basket = mushroom.basket
            basket.mushrooms.remove(mushroom)
            session.commit()
            return Basket.model_validate(basket)

    @staticmethod
    def get_basket(basket_id: int):
        with session_factory() as session:
            basket = get_or_404(session, BasketDB, basket_id, 'Корзина')
            return Basket.model_validate(basket)
