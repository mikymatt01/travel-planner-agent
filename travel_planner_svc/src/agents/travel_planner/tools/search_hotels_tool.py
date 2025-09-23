from pydantic import BaseModel, Field
from utils.db import hotel_collection
from crewai.tools import BaseTool
from typing import Type
from src.plugins.hotel import hotel_repository, hotel_pydantic
class SearchHotelsInput(BaseModel):
    """Input schema for SearchHotels."""
    start_date: str = Field(..., description="The start date for the check-in.")
    end_date: str = Field(..., description="The end date for the check-out.")
    to_location: str = Field(..., description="The arrival location for the flight search.")

class SearchHotels(BaseTool):
    name: str = "SearchHotels"
    description: str = (
        "A tool to search for hotels and bnb based on given criteria."
    )
    args_schema: Type[BaseModel] = SearchHotelsInput
    
    def _run(
        self,
        start_date: str,
        end_date: str,
        to_location: str
    ) -> str:
        print(f"Searching for hotels and bnb in {to_location} between {start_date} and {end_date}...")
        
        hotels = hotel_repository.search(
            body=hotel_pydantic.HotelSearchInput(
                location=to_location,
                type="HOTEL"
            )
        )
        
        bnbs = hotel_repository.search(
            body=hotel_pydantic.HotelSearchInput(
                location=to_location,
                type="BNB"
            )
        )

        return {
            "city": to_location,
            "hotels": [hotel for hotel in hotels],
            "bnbs": [bnb for bnb in bnbs]
        }