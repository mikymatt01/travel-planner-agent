from typing import Type, Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from math_eval import safe_compute

class MathInput(BaseModel):
    """Input schema for PaymentTool."""
    expression: str = Field(..., description="The mathematical expression to evaluate")


class MathTool(BaseTool):
    name: str = "MathTool"
    description: str = (
        '''
        A tool that evaluates mathematical expressions and returns the result.
        '''
    )
    args_schema: Type[BaseModel] = MathInput

    def _run(
        self,
        expression: Optional[str],
    ) -> str:
        """
        Run the math tool.
        """
        try:
            print("start math tool", expression)
            result = safe_compute(expression)
            print("end payment tool")
            return result
        except Exception as e:
            raise Exception(f"An error occurred while running the math tool: {e}")
