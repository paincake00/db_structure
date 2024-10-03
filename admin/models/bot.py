from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from models.db_session import Base


class Bot(Base):
    __tablename__ = "bots"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    token: Mapped[str]
    group_id: Mapped[int] = mapped_column(BigInteger)
    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"))

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()