from fastapi import FastAPI
from db import events_collection
from pydantic import BaseModel

class EventModel(BaseModel):
    title: str
    description: str


app = FastAPI()

@app.get("/")
def get_home():
    return { "message": "You are on the home page"}

# Events endpoints
@app.get("/events")
def get_events():
    # Get all events from database
    events = events_collection.find().to_list()
    # Return response
    return {"data": events}

@app.post("/events")
def post_event(event: EventModel):
    # Insert event into database
    events_collection.insert_one(event.model_dump())
    # Return response
    return {"message": "Event added successfully"}


@app.get("/events/{event_id}")
def get_event_by_id(event_id):
    # Get event from database by id
    event = events_collection.find_one({"_id": event_id})
    # Return response
    return { "data": event}

