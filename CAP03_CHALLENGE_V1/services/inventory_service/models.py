from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    room_type = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    available = Column(Boolean, default=True)

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, index=True)
    date = Column(String, index=True)
    available_count = Column(Integer)