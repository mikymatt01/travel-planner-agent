from crewai.events import (
    CrewKickoffStartedEvent,
    CrewKickoffCompletedEvent,
    AgentExecutionCompletedEvent
)
from crewai.events import BaseEventListener
from utils.socket_sender import WebsocketSender, Type
import asyncio

class CrewListener(BaseEventListener):
    def __init__(self, websocket=None):
        super().__init__()
        self.websocket = websocket
    
    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(CrewKickoffStartedEvent)
        def on_crew_started(source, event):
            print(f"Crew '{event.crew_name}' has started execution!")

        @crewai_event_bus.on(CrewKickoffCompletedEvent)
        def on_crew_completed(source, event):
            print(f"Crew '{event.crew_name}' has completed execution!")
            print(f"Output: {event.output}")

        # @crewai_event_bus.on(AgentExecutionStartedEvent)
        # def on_agent_execution_started(source, event):
        #     print(f"Agent '{event.agent.role}' started task")
        #     print(f"Output: {event.output}")
            
        @crewai_event_bus.on(AgentExecutionCompletedEvent)
        def on_agent_execution_completed(source, event):
            print(f"Agent '{event.agent.role}' completed task")
            print(f"Output: {event.output}")
            print('Creating new event loop to send message')
            self.notify(event.agent.role.replace('\n', ''))
        
    async def send_message(
        self,
        agent
    ) -> str:
        await WebsocketSender.send(self.websocket, f'{agent} is working on it...', type=Type.LOG)

    def notify(self, agent) -> str:
        """Run async code in a new event loop"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(
            self.send_message(agent)
        )
        loop.close()
        return result