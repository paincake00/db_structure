from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.db_session import Base


class AdminTariff(Base):
    __tablename__ = "admin_tariffs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count_users: Mapped[int]
    price: Mapped[float]
    bot_id: Mapped[int] = mapped_column(ForeignKey("bots.id"))

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()