from datetime import datetime, timedelta
from utils.db import flight_collection
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from typing import Type
from src.plugins.flight import flight_repository, flight_pydantic

class SearchFlightsInput(BaseModel):
    """Input schema for SearchFlights."""
    start_date: str = Field(..., description="The start date for the flight search for the outbound_flight. E.g., '2025-06-01'")
    end_date: str = Field(..., description="The end date for the flight search for the return_flight. E.g., '2025-06-01'")
    from_location: str = Field(..., description="The departure city for the flight search. E.g., 'New York'")
    to_location: str = Field(..., description="The arrival city for the flight search. E.g., 'Los Angeles'")


class SearchFlights(BaseTool):
    name: str = "SearchFlights"
    description: str = (
        "A tool to search for flights based on given criteria."
    )
    args_schema: Type[BaseModel] = SearchFlightsInput

    def _run(
        self,
        start_date: str,
        end_date: str,
        from_location: str,
        to_location: str
    ) -> str:
        print(f"Searching for flights from {from_location} to {to_location} between {start_date} and {end_date}...")
            
        outbound_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        outbound_end_date = outbound_start_date + timedelta(days=1)
        
        outbound = flight_repository.search(
            body=flight_pydantic.FlightSearchInput(
                type="Departure",
                start_date=outbound_start_date,
                end_date=outbound_end_date,
                from_location=from_location,
                to_location=to_location
            )
        )
        
        inbound_start_date = datetime.strptime(end_date, "%Y-%m-%d")
        inbound_end_date = inbound_start_date + timedelta(days=1)


        inbound = flight_repository.search(
            body=flight_pydantic.FlightSearchInput(
                type="Arrival",
                start_date=inbound_start_date,
                end_date=inbound_end_date,
                from_location=from_location,
                to_location=to_location
            )
        )

        return {
            "departure_location": from_location,
            "arrival_location": to_location,
            "outbound_flights": [flight for flight in outbound],
            "inbound_flights": [flight for flight in inbound]
        }
            
