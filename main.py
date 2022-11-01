import uvicorn
from fastapi import FastAPI, Request

from configuration import app_logger
import repositories
from services import accounts_service

app = FastAPI()

app.include_router(accounts_service.router)

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


# @app.exception_handler(Exception)
# async def exception_handler(request: Request, exc: Exception):
#     app_logger.error(f"Error: {exc}")


if __name__ == "__main__":
    app_logger.debug("APP START")

    app_logger.info("Initialising databases")
    repositories.init_databases()

    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO add models Event, Community, Channel
# TODO add code for storage layer (postgresql, psycopg3)
