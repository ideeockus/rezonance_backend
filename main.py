from fastapi import FastAPI

app = FastAPI()

"""
representation layer
domain layer 
storage layer
"""


@app.get("/")
async def abc():
    return {"abc": "123"}
