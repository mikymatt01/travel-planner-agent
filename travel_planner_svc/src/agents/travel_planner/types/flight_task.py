from pydantic import BaseModel, Field
from typing import List

class Flight(BaseModel):
    flight_number: str = Field(..., description="Flight number")
    departure: str = Field(..., description="Departure YYYY-MM-DD hh:mm")
    arrival: str = Field(..., description="Arrival YYYY-MM-DD hh:mm")
    stops: str = Field(..., description="Number of stops")
    airline: str = Field(..., description="Airline name")
    price: str = Field(..., description="Price of the flight")
    duration: str = Field(..., description="Duration of the flight")
    from_location: str = Field(..., description="Departure location, e.g., 'New York'")
    to_location: str = Field(..., description="Arrival location, e.g., 'Tokyo'")

class FlightOutput(BaseModel):
    departure_location: str = Field(..., description="Departure location")
    arrival_location: str = Field(..., description="Arrival location")
    outbound_flights: List[Flight] = Field(..., description="List of outbound flight options")
    inbound_flights: List[Flight] = Field(..., description="List of inbound flight options")