from pydantic import BaseModel, Field
from typing import List

class FlightnputPreferences(BaseModel):
    budget: float = Field(..., description="Budget preference.")
    cabin: str = Field(..., description="Cabin class preference. E.g., economy, business")
    max_stops: int = Field(..., description="Number of stops.")
    
class FlightInput(BaseModel):
    departure_location: str = Field(..., description="Departure city. E.g., New York")
    arrival_location: str = Field(..., description="Arrival city. E.g., Tokyo")
    departure_date: str = Field(..., description="Departure date in YYYY-MM-DD format. E.g., 2025-06-01")
    return_date: str = Field(..., description="Return date in YYYY-MM-DD format. E.g., 2025-06-10")
    preferences: FlightnputPreferences = Field(..., description="Flight preferences.")

class FlightTask(BaseModel):
    type: str = Field(..., description="Type of the task. E.g., flight_task")
    assigned_agent: str = Field(..., description="Name of the agent assigned to the task. E.g., flight_researcher")
    status: str = Field(..., description="PENDING")
    input: FlightInput = Field(..., description="Flight task input details.")


class HotelInputPreferences(BaseModel):
    max_price_per_night: float = Field(..., description="Budget preference.")
    number_of_nights: float = Field(..., description="Number of nights to stay.")
    room_type: str = Field(..., description="Room type preference. E.g., single, double")
    rating_min: int = Field(..., description="Minimum hotel rating. E.g., 3")
    
class HotelInput(BaseModel):
    city: str = Field(..., description="city location. E.g., Tokyo")
    check_in_date: str = Field(..., description="Check-in date in YYYY-MM-DD hh:mm format. E.g., 2025-06-10 10:30")
    check_out_date: str = Field(..., description="Check-out date in YYYY-MM-DD hh:mm format. E.g., 2025-06-20 11:30")
    preferences: HotelInputPreferences = Field(..., description="Hotel preferences.")

class HotelTask(BaseModel):
    type: str = Field(..., description="Type of the task. E.g., hotel_task")
    assigned_agent: str = Field(..., description="Name of the agent assigned to the task. E.g., hotel_researcher")
    status: str = Field(..., description="PENDING")
    input: HotelInput = Field(..., description="Hotel task input details.")

class TravelOutput(BaseModel):
    status: str = Field(..., description="Status of the travel planning task. E.g., IN_PROGRESS")
    flight_task: FlightTask = Field(..., description="Details of the flight task.")
    hotel_task: HotelTask = Field(..., description="Details of the hotel task.")