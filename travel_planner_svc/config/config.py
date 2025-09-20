from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PARKING = os.getenv('PARKING')
SUSHI = os.getenv('SUSHI')