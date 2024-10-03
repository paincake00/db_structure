from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.db_session import Base


class UserTariff(Base):
    __tablename__ = "user_tariffs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    bot_id: Mapped[int] = mapped_column(ForeignKey("bots.id"))
    price: Mapped[float]
    days: Mapped[int]

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()