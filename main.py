from Project import *
from fastapi import FastAPI
from Project.Services.chatBot import templateMessage
# from router import train

# app = FastAPI()
# app.include_router(
#     train.router,
#     prefix="/train"
# )
from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return "This api For Line Chat"