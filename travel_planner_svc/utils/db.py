import os
import json
import mongomock
from datetime import datetime

with open('utils/flights.json') as f:
    flights = json.load(f)

with open('utils/hotels.json') as f:
    hotels = json.load(f)

for doc in flights:
    if "departure" in doc:
        doc["departure"] = datetime.fromisoformat(doc["departure"])
    if "arrival" in doc:
        doc["arrival"] = datetime.fromisoformat(doc["arrival"])


client = mongomock.MongoClient()
db = client['testdb']

flight_collection = db['flight']
hotel_collection = db['hotel']

flight_collection.insert_many(flights)
hotel_collection.insert_many(hotels)