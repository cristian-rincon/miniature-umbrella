from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/myappdb"  # point to the db service in the docker-compose.yml file
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base = declarative_base()
except Exception as e:
    print(e)
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

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

@app.post("/cars/", response_model=CarResponse)
def create_car(car: CarCreate):
    db = SessionLocal()
    db_car = Car(brand=car.brand, model=car.model, year=car.year)
    print(db_car)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.get("/cars/{car_id}", response_model=CarResponse)
def read_car(car_id: int):
    db = SessionLocal()
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car