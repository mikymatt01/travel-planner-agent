from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from agents.travel_planner.crew import TravelPlanner
from typing import Type

class TravelPlannerInput(BaseModel):
    """Input schema for TravelPlanner."""
    start_date: str = Field(..., description="The start date for the flight search for the outbound_flight.")
    end_date: str = Field(..., description="The end date for the flight search for the return_flight.")
    from_location: str = Field(..., description="The departure location for the flight search.")
    to_location: str = Field(..., description="The arrival location for the flight search.")


class TravelPlannerTool(BaseTool):
    name: str = "TravelPlanner"
    description: str = (
        '''
        A tool to plan a trip based on given criteria.
        This tool uses a crew to search for flights and hotels.
        The crew consists of two tasks: SearchFlights and SearchHotels.
        '''
    )
    args_schema: Type[BaseModel] = TravelPlannerInput
    
    def _run(
        self,
        start_date: str,
        end_date: str,
        from_location: str,
        to_location: str
    ) -> str:
        inputs = {
            "start_date": start_date,
            "return_date": end_date,
            "from": from_location,
            "to": to_location
        }
        try:
            print("start travel planner crew tool")
            result = TravelPlanner().crew().kickoff(inputs=inputs)
            print("end travel planner crew tool")
            return result.tasks_output
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")
