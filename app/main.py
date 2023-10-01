from fastapi import FastAPI, HTTPException
from loguru import logger
from sqlalchemy.orm import sessionmaker
from app.database import Base,engine
from app.models import Car, CarCreate, CarResponse

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

app = FastAPI()

@app.post("/cars/", response_model=CarResponse)
def create_car(car: CarCreate):
    db_car = Car(brand=car.brand, model=car.model, year=car.year)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    logger.info(f"Created car {db_car.id}")
    return db_car


@app.get("/cars/{car_id}", response_model=CarResponse)
def read_car(car_id: int):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    logger.info(f"Read car {db_car.id}")
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
