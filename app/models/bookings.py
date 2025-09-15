from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Integer
from datetime import datetime
from app.core.database import Base

class Booking(Base):
    """
    SQLAlchemy ORM model for storing interview or appointment bookings.

    Each booking stores user details along with the scheduled date and time.

    Attributes:
        id (int): Primary key, auto-incremented, indexed for faster queries.
        name (str): Full name of the person making the booking.
        email (str): Email address of the person making the booking.
        date (str): Scheduled date for the booking (format: YYYY-MM-DD).
        time (str): Scheduled time for the booking (format: HH:MM).
        created_at (datetime): Timestamp when the booking record was created.
    """

    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    date: Mapped[str] = mapped_column(String(20), nullable=False)
    time: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
