from utils.db import flight_collection
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from typing import Type

class SearchFlightInput(BaseModel):
    """Input schema for SearchFlight."""
    flight_number: str = Field(..., description="The unique identifier of the flight.")

class SearchFlight(BaseTool):
    name: str = "SearchFlights"
    description: str = (
        "A tool to search for flights based on given criteria."
    )
    args_schema: Type[BaseModel] = SearchFlightInput
    

    def _run(
        self,
        flight_number: str
    ) -> str:
        print(f"Searching for flight with flight_number {flight_number}...")
        
        flight = flight_collection.find_one({"flight_number": flight_number})
        if flight:
            return flight
        else:
            return f"No flight found with ID {flight_number}."
            
