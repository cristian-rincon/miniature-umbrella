from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)


# Pydantic models
class CarCreate(BaseModel):
    brand: str
    model: str
    year: int

    class Config:
        orm_mode = True


class CarResponse(CarCreate):
    id: int

    class Config:
        orm_mode = True
