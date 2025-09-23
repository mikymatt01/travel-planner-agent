from pydantic import BaseModel, Field

class HotelSearchInput(BaseModel):
    """Input schema for FlightSearchInput."""
    location: str = Field(..., description="The location to search hotels in. E.g., 'New York'")
    type: str = Field(..., description="The type of accommodation. E.g., 'HOTEL' or 'BNB'")
