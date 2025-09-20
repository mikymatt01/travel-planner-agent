from typing import Type, Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class PaymentInput(BaseModel):
    """Input schema for PaymentTool."""
    hotel_name: Optional[str] = Field(..., description="The hotel name choosen by the user")
    inbound_flight_number: Optional[str] = Field(..., description="The inbound flight number choosen by the user")
    outbound_flight_number: Optional[str] = Field(..., description="The outbound flight number choosen by the user")


class PaymentTool(BaseTool):
    name: str = "PaymentTool"
    description: str = (
        '''
        A tool that helps to book the hotel and flights by taking
        the hotel name, inbound flight number, and outbound flight number as inputs.
        '''
    )
    args_schema: Type[BaseModel] = PaymentInput
    
    def _run(
        self,
        hotel_name: Optional[str],
        inbound_flight_number: Optional[str],
        outbound_flight_number: Optional[str],
    ) -> str:
        inputs = {
            "hotel_name": hotel_name,
            "inbound_flight_number": inbound_flight_number,
            "outbound_flight_number": outbound_flight_number,
        }
        try:
            print("start payment tool", inputs)
            result = 'https://stripe.com/payment-example'
            print("end payment tool")
            return result
        except Exception as e:
            raise Exception(f"An error occurred while running the payment tool: {e}")
