from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from travel_planner.tools.search_flights_tool import SearchFlights
from travel_planner.tools.search_hotels_tool import SearchHotels
from crewai.memory.external.external_memory import ExternalMemory
from .tools.travel_planner_tool import TravelPlannerTool
from .tools.payment_tool import PaymentTool
from crewai import Crew, Agent, Process, Task
from .tools.math_tool import MathTool
from .memory import CustomStorage
from typing import List

custom_storage = CustomStorage()

travel_planner_tool = TravelPlannerTool()
search_flights_tool = SearchFlights()
search_hotels_tool = SearchHotels()
payment_tool = PaymentTool()
math_tool = MathTool()

@CrewBase
class TravelSupportCrew:
    """A crew that assists users with travel planning, including booking flights and accommodations."""
    agents: List[BaseAgent]
    tasks: List[Task]
    
    @agent
    def chatbot_agent(self):
        return Agent(
            config=self.agents_config['chatbot_agent'],
            tools=[
                travel_planner_tool,
                search_flights_tool,
                search_hotels_tool,
                payment_tool,
                math_tool
            ],
            verbose=True,
            memory=True,
        )
        
    @task
    def user_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        external_memory = ExternalMemory(storage=custom_storage)
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            external_memory=external_memory,
            verbose=True
        )