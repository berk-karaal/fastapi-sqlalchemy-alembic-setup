from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
    deleted_at: Mapped[datetime | None]

    def __repr__(self) -> str:
        return f"Todo(id={self.id})"
