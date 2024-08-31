from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_router, event_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
