from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routes import user_router, event_router
from database.connections import conn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def root():
    return RedirectResponse(url="/event")

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
