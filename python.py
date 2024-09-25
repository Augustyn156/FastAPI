from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

car_db = []
car_ratings_db = {}

class Car(BaseModel):
    marka: str
    model: str
    rok_prod: int

class Rate(BaseModel):
    rating: int


@app.post("/cars/")
def add_car(car: Car):
    car.id=len(car_db)+1
    car.append(car_db)
    car_ratings_db.append
    car_ratings_db[car.id] = []
    return car

@app.post("/cars/{car_id}/rate")
def rate_car(car_id: int, rate: Rate):
    if car_id > len(car_db) or car_id <= 0:
        raise HTTPException(status_code=404, 
                            detail="Nie ma samochodu o takim id")
    
    if rate.rating<1 or rate.rating>5:
        raise HTTPException(status_code=400, 
                            detail="Ocena musi być liczbą od 1 do 5")
    
    car_ratings_db[car_id].append(rate.rating)

    return rate

@app.get("cars/top10")
def get_top10():

    cars_with_ratings=[]

    for car in car_db:
        for car_ratings_db[car.id]:
            cars_with_ratings.append({
                "id":car.id,
                "marka":car.marka,
                "model":car.model,
                "rok_prod":car.rok_prod,
                "rating":rating
            })
    top_cars =sorted(cars_with_ratings, key=lambda x: x.rating, reverse=True)
    return top_cars