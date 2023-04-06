import sys

from fastapi import FastAPI
from pydantic import BaseModel

# giving the app var is used as a funtion in the behave tests,
# we need to transform it into a lambda function that calls FastAPI()
# and returns the app in a given port

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class ResponseMessage(BaseModel):
    message: str


@app.get("/")
def read_root():
    """This is the root endpoint"""
    response = {"Hello": "World"}, 200
    return response


@app.post("/shutdown")
async def shutdown():
    """This is the shutdown endpoint"""
    sys.exit("Shutting down")
