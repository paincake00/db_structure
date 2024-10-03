from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, func, String, Date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column, Mapped, Session

from models.db_session import Base


class TelegramUser(Base):
    __tablename__ = "telegram_users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    username: Mapped[Optional[str]]
    start_date: Mapped[Date] = mapped_column(Date, default=datetime.now)

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()