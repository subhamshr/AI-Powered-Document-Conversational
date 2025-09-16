from pydantic import BaseModel, EmailStr

class BookingCreate(BaseModel):
    """
    Pydantic model for creating a new booking.

    Attributes:
        name (str): Full name of the user making the booking.
        email (EmailStr): Email address of the user (validated as proper email).
        date (str): Scheduled date for the booking (format: YYYY-MM-DD).
        time (str): Scheduled time for the booking (format: HH:MM).
    """
    name: str
    email: EmailStr
    date: str
    time: str

class BookingResponse(BookingCreate):
    """
    Pydantic model for returning booking information in API responses.

    Inherits all fields from BookingCreate and adds:
        id (int): Unique identifier of the booking.
        created_at (str): Timestamp when the booking was created.
    """
    id: int
    created_at: str
    
    
    
    