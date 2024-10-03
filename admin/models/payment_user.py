from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, func, Date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.db_session import Base


class PaymentUser(Base):
    __tablename__ = "payment_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float]
    current_date: Mapped[Date] = mapped_column(Date, default=datetime.now)
    count_days: Mapped[int]
    promo_id: Mapped[Optional[int]] = mapped_column(ForeignKey("promos.id"))
    tariff_id: Mapped[int] = mapped_column(ForeignKey("user_tariffs.id"))

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
