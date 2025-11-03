from utils.db import flight_collection
from .flight_pydantic import FlightSearchInput

def get(flight_number: str):
    return flight_collection.find_one({"flight_number": flight_number})

def all():
    return list(flight_collection.find())

def search(
    body: FlightSearchInput
):
    result = []
    
    print({
            "departure": {"$gte": body.start_date, "$lt": body.end_date},
            "from_location": {"$regex": body.from_location, "$options": "i"},
            "to_location": {"$regex": body.to_location, "$options": "i"},
        })
    if body.type == "Departure":
        result = flight_collection.find({
            "departure": {"$gte": body.start_date, "$lt": body.end_date},
            "from_location": {"$regex": body.from_location, "$options": "i"},
            "to_location": {"$regex": body.to_location, "$options": "i"},
        }).sort({ "price": 1, "duration": 1 })
    
    elif body.type == "Arrival":
        result = flight_collection.find({
            "arrival": {"$gte": body.start_date, "$lt": body.end_date},
            "from_location": {"$regex": body.to_location, "$options": "i"},
            "to_location": {"$regex": body.from_location, "$options": "i"},
        }).sort({ "price": 1, "duration": 1 })
    
    return list(result)