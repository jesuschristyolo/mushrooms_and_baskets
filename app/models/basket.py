from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db_engine import Base
from sqlalchemy import String
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum


class FreshnessEnum(Enum):
    very_fresh = "very_fresh"
    normal_fresh = "normal_fresh"
    stale = "stale"


freshness_enum = SQLAlchemyEnum(FreshnessEnum, name="freshnessenum")


class BasketDB(Base):
    __tablename__ = 'baskets'
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_name: Mapped[str] = mapped_column(String(200))
    capacity: Mapped[float] = mapped_column()

    mushrooms = relationship("MushroomDB", back_populates="basket")
