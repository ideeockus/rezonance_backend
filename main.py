import uvicorn
from fastapi import FastAPI

from configuration import app_logger
import repositories
from services import auth_service

app = FastAPI()

app.include_router(auth_service.router)

"""
representation layer
domain layer 
storage layer
"""


@app.get("/")
async def root():
    return {"abc": "123"}


@app.on_event("startup")
def open_pool():
    app_logger.info("Server is UP")


@app.on_event("shutdown")
def close_pool():
    app_logger.info("Server is DOWN")


if __name__ == "__main__":
    app_logger.debug("APP START")

    app_logger.info("Initialising databases")
    repositories.init_databases()

    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO add models Event, Community, Channel
# TODO add code for storage layer (postgresql, psycopg3)
