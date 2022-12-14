from fastapi import FastAPI
from auth import authentication
from router import user, room, reception, mobile_app
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(room.router)
app.include_router(reception.router)
app.include_router(mobile_app.router)


if __name__ == "__main__":
    uvicorn.run(app)