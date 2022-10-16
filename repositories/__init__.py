import psycopg

from configuration import app_logger, ServiceConfig

conn = psycopg.connect(
    ServiceConfig.POSTGRES_DB_URL,
    # row_factory=namedtuple_row
)


def init_accounts_db():
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS accounts (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
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

# logging.info("Initialising database")

# TODO add psycopg ConnectionPool instead of making connection for each repository
