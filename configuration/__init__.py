import os


class ServiceConfig:
    postgres_db_url = os.getenv("POSTGRES_DB_URL")
