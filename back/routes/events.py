from fastapi import APIRouter, HTTPException, status, Body, Depends
from database.connections import get_session
from typing import List
from sqlmodel import select

from models.events import Event, EventUpdate


event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.delete("")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }

@event_router.get("")
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrive_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID doesn't exist"
    )


@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return{
                "message": "Event deleted successfully"
            }
    
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.put("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return{
        "message": "Event created successfully"
    }

@event_router.post("/new")
async def create_event(new_event: Event, session = Depends(get_session)) -> dict:
        session.add(new_event)
        session.commit()
        session.refresh(new_event)

        return {
            "message": "Event created successfuly"
        }




        