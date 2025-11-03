from fastapi import APIRouter
from datetime import datetime, timedelta
from . import flight_repository, flight_pydantic

router = APIRouter()

@router.get("/flights/search")
def search(start_date: str, from_location: str, to_location: str):
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
    
    print(f"Found {len(outbound)} outbound flights from {from_location} to {to_location} on {start_date}.")
    return {
        "departure_location": from_location,
        "arrival_location": to_location,
        "outbound_flights": [flight for flight in outbound]
    }