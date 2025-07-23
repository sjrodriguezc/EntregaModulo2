from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String, default='pending')  # pending, confirmed, cancelled

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    room_type = Column(String)
    price = Column(Integer)
    availability = Column(Integer)  # Number of available rooms

    bookings = relationship("Booking", back_populates="room")