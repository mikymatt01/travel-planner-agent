from utils.db import hotel_collection
from .hotel_pydantic import HotelSearchInput

def search(body: HotelSearchInput):
    return list(hotel_collection.find({
        "location": {"$regex": body.location, "$options": "i"},
        "type": body.type
    }))
