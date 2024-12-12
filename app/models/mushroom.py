from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db_engine import Base
from sqlalchemy import String, ForeignKey, Column
from app.models.basket import freshness_enum


class MushroomDB(Base):
    __tablename__ = 'mushrooms'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    edibility: Mapped[bool] = mapped_column()
    weight: Mapped[float] = mapped_column()
    freshness = Column(freshness_enum)
    basket_id: Mapped[Optional[int]] = mapped_column(ForeignKey("baskets.id", ondelete='SET NULL'))

    basket = relationship("BasketDB", back_populates="mushrooms")
