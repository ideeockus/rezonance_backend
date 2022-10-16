import logging
import os
import sys


class ServiceConfig:
    """Service configurations from ENV"""

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")

    POSTGRES_DB_URL = f"postgres://{DB_USER}@localhost/{DB_NAME}"
    # postgres_db_url = os.getenv("POSTGRES_DB_URL")


app_logging_formatter = logging.Formatter(
    fmt="%(asctime)s| %(levelname).1s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

app_logging_handler = logging.StreamHandler(sys.stdout)
app_logging_handler.setFormatter(app_logging_formatter)

LOG_LEVEL = logging.DEBUG
app_logger = logging.getLogger("app_logger")
app_logger.setLevel(LOG_LEVEL)
app_logger.addHandler(app_logging_handler)
