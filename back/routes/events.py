from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connections import get_session
from sqlmodel import select
from models.events import *

event_router = APIRouter(
    tags=["Events"]
)

# 생성
@event_router.post("/new")
async def create_event(new_event: Event,
                       session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh()

    return{
        "message": "Event created succsessfully"
    }

# 읽어오기
@event_router.get("/", response_model= List[Event])
async def retrieve_all_events(session = Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

# 특정부분 읽어오기
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session = Depends(get_session))-> Event:
    event = session.get(Event,id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.put("/edit/{id}")
async def update_event(id: int, new_data: EventUpdate, session = Depends(get_session)) -> Event:
    event = session.get(Event,id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key,value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

