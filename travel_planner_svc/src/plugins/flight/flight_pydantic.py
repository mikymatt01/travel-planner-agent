from pydantic import BaseModel, Field
from typing import Optional

class FlightSearchInput(BaseModel):
    """Input schema for FlightSearchInput."""
    type: Optional[str] = Field(..., description="The departure city for the flight. E.g., 'Departure' or 'Arrival'")
    start_date: str = Field(..., description="The start date for the flight search for the outbound_flight. E.g., '2025-06-01'")
    end_date: str = Field(..., description="The end date for the flight search for the return_flight. E.g., '2025-06-01'")
    from_location: str = Field(..., description="The departure city for the flight search. E.g., 'New York'")
    to_location: str = Field(..., description="The arrival city for the flight search. E.g., 'Los Angeles'")
