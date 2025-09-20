from pydantic import BaseModel, Field
from typing import List

class Hotel(BaseModel):
    id: str = Field(..., description="Unique identifier for the hotel")
    type: str = Field(..., description="Type of accommodation, e.g., 'HOTEL' or 'BNB'")
    name: str = Field(..., description="Name of the hotel")
    location: str = Field(..., description="Location of the hotel")
    price_per_night: float = Field(..., description="Price per night")
    total_price: float = Field(..., description="Price per night multiplied by number of nights")
    rating: int = Field(..., description="Rating of the hotel")
    amenities: List[str] = Field(..., description="List of amenities offered by the hotel")

class HotelOutput(BaseModel):
    city: str = Field(..., description="City where the hotel/bnb is located")
    hotels: List[Hotel] = Field(..., description="List of hotel options")
    bnbs: List[Hotel] = Field(..., description="List of bnb options")