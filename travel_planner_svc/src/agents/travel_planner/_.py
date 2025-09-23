#!/usr/bin/env python
import sys
import warnings
from travel_planner.crew import TravelPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "start_date": "2025-06-01",
        "return_date": "2025-06-10",
        "from": "Naples",
        "to": "Tokyo"
    }
    try:
        print("Running the crew with inputs: ", inputs)
        TravelPlanner().crew().kickoff(inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "start_date": "2025-06-01",
        "return_date": "2025-06-10",
        "from": "Naples",
        "to": "Tokyo"
    }
    try:
        TravelPlanner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelPlanner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "start_date": "2025-06-01",
        "return_date": "2025-06-10",
        "from": "Naples",
        "to": "Tokyo"
    }
    
    try:
        TravelPlanner().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
