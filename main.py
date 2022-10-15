from fastapi import FastAPI

from configuration import app_logger
import repositories

app = FastAPI()

"""
representation layer
domain layer 
storage layer
"""


@app.get("/")
async def abc():
    return {"abc": "123"}


app_logger.debug("APP START")
# TODO add README
# TODO add LICENCE

# TODO add models Event, Community, Channel
# TODO add code for storage layer (postgresql, psycopg3)
