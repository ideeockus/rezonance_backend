from typing import Optional
from uuid import UUID

import psycopg
from psycopg.rows import class_row

from configuration import ServiceConfig, app_logger
from models.account import Account, UserData, Contacts

conn = psycopg.connect(
    ServiceConfig.POSTGRES_DB_URL,
    # row_factory=class_row(Account)
)

# aconn = psycopg.AsyncConnection.connect(ServiceConfig.POSTGRES_DB_URL)
# async with conn.cursor() as cur:
#     cur.execute(...)


def create_account(username: str, user_data: UserData, contacts: Contacts) -> Optional[UUID]:
    """create an account and return id"""
    app_logger.debug(f"creating account {username}")
    try:
        # # # should it raise exception or return None ?!
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO accounts (username, user_data, contacts)
                VALUES (%(username)s, %(user_data)s, %(contacts)s)
                RETURNING id;
                """,
                {
                    "username": username,
                    "user_data": user_data.json(),
                    "contacts": contacts.json(),
                },
            )
            account_id = cur.fetchone()[0]

            conn.commit()
            return account_id
            # # #
    except psycopg.errors.Error:
        conn.rollback()  # need to rollback in case of exception
        return None

# TODO table to safely remove accounts


def get_account_by_username(username: str) -> Optional[Account]:
    app_logger.debug(f"getting account by username {username}")
    with conn.cursor(row_factory=class_row(Account)) as cur:
        cur.execute(
            "SELECT * FROM accounts WHERE username = %(username)s;",
            {"username": username},
        )
        account = cur.fetchone()

        if not account:
            # raise KeyError(f"User {username} not found")
            return None

        return account


def get_account_by_id(account_id: UUID) -> Optional[Account]:
    app_logger.debug(f"getting account by account_id {account_id}")
    with conn.cursor(row_factory=class_row(Account)) as cur:
        cur.execute(
            "SELECT * FROM accounts WHERE id = %(account_id)s;",
            {"account_id": account_id},
        )
        account = cur.fetchone()

        if not account:
            return None

        return account


def delete_account_by_id(account_id: UUID) -> bool:
    app_logger.debug(f"deleting account by account_id {account_id}")
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM accounts WHERE id = %(account_id)s"
            "RETURNING id;",
            {"account_id": account_id},
        )
        conn.commit()

        result = cur.fetchall()

        if not result:
            return False

        return True
