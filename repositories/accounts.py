import psycopg
from psycopg.rows import class_row

from models.account import Account


def add_account(account: Account) -> int:
    """create an account and return id"""
    # TODO psycopg add accout
    # "INSERT ..."
    # with psycopg.connect("dbname=")

# TODO add methods:
#     get_account_by_id
#     get_account_by_username


def get_account_by_username(username: str) -> Account:
    with psycopg.connect("dbname=rezonance_local_db user=rezonance_local_user") as conn:
        with conn.cursor(row_factory=class_row(Account)) as cur:
            cur.execute(
                "SELECT * FROM users WHERE username = %(username)s;",
                {"username": username},
            )
            obj = cur.fetchone()

            if not obj:
                raise KeyError(f"User {username} not found")

            return obj
