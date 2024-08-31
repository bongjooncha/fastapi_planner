from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id:int
    title: str
    image: str
    descritpion: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "id" : 1,
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }