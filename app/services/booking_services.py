from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.bookings import Booking
from app.schema.booking_schema import BookingCreate
from datetime import datetime, timezone
from fastapi import UploadFile,FastAPI,APIRouter,File,status,Form,HTTPException
from app.core.config import settings

async def create_booking(session: AsyncSession, booking: BookingCreate):
    """
    Create a new booking record in the database.

    This function takes a BookingCreate schema object, inserts it into the
    bookings table, commits the transaction, and refreshes the object to
    return the newly created booking with its generated ID and timestamps.

    Args:
        session (AsyncSession): Async SQLAlchemy session for database operations.
        booking (BookingCreate): Pydantic model containing booking details.

    Returns:
        Booking: The newly created Booking ORM object, including auto-generated fields like `id` and `created_at`.
    """
    db_booking = Booking(
        name=booking.name,
        email=booking.email,
        date=booking.date,
        time=booking.time,

    )
    session.add(db_booking)
    await session.commit()
    await session.refresh(db_booking)
    return db_booking

