from sqlalchemy.orm import Mapped, mapped_column

from api import db
from api.db import Base


class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
