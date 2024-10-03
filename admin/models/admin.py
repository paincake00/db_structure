from sqlalchemy import ForeignKey, Date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.db_session import Base

class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(ForeignKey("telegram_users.id"))
    tariff_id: Mapped[int] = mapped_column(ForeignKey("admin_tariffs.id"))
    expire_date: Mapped[Date] = mapped_column(Date)

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()