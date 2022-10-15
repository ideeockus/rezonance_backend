import logging

import psycopg

from configuration import app_logger

conn = psycopg.connect(
    "dbname=rezonance_local_db user=rezonance_local_user",
    # row_factory=namedtuple_row
)


def init_accounts_db():
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS accounts (
            id INT PRIMARY KEY,
            username VARCHAR UNIQUE,
            user_data JSONB,
            contacts JSONB
            );
            """
        )
        app_logger.debug("accounts db initialised")
        conn.commit()


def init_databases():
    init_accounts_db()


app_logger.info("Initialising databases")
init_databases()
# logging.info("Initialising database")
