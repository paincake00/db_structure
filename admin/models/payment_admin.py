from datetime import datetime

from sqlalchemy import ForeignKey, func, Date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.db_session import Base


class PaymentAdmin(Base):
    __tablename__ = "payment_admins"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"))
    amount: Mapped[float]
    current_date: Mapped[Date] = mapped_column(Date, default=datetime.now)
    tariff_id: Mapped[int] = mapped_column(ForeignKey("admin_tariffs.id"))

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
