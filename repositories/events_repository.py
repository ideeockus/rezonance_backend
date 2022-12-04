from datetime import datetime
from typing import Optional
from uuid import UUID

import psycopg
from psycopg.rows import class_row
from passlib.context import CryptContext

from configuration import ServiceConfig, app_logger
from models.account import Account, UserData, Contacts
from models.event import Event, EventType
from models.other import Location

conn = psycopg.connect(
    ServiceConfig.POSTGRES_DB_URL,
)


def create_event(event_name: str, description: str, date: datetime,
                 event_type: EventType, location: Location) -> Optional[UUID]:
    """create an account and return id"""
    app_logger.debug(f"creating event {event_name}")
    try:
        # # # should it raise exception or return None ?!
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO events (name, description, date, contacts)
                VALUES (%(username)s, %(password_hash)s, %(user_data)s, %(contacts)s)
                RETURNING id;
                """,
                {
                    "username": username,
                    "password_hash": password_hash,
                    "user_data": user_data.json(),
                    "contacts": contacts.json(),
                },
            )
            account_id = cur.fetchone()[0]

            conn.commit()
            return account_id
            # # #
    except psycopg.errors.UniqueViolation:
        app_logger.error(f"Username {username} exists")
        return None
    except psycopg.errors.Error as e:
        app_logger.exception(f"error: {e}")
        conn.rollback()  # need to rollback in case of exception
        return None

#
# def get_account_by_credentials(username: str, password: str) -> Optional[Account]:
#     app_logger.debug(f"authenticationg account {username}")
#
#     # password_hash = pwd_context.hash(password)
#
#     with conn.cursor(row_factory=class_row(Account)) as cur:
#         cur.execute(
#             "SELECT * FROM accounts WHERE "
#             "username = %(username)s;",
#             {"username": username},
#         )
#         account = cur.fetchone()
#
#         if not account:
#             # raise KeyError(f"User {username} not found")
#             return None
#
#         # checking password
#         if pwd_context.verify(password, account.password_hash):
#             return account
#
#         return None
#
#     # with conn.cursor() as cur:
#     #     cur.execute(
#     #         """
#     #         SELECT * FROM accounts
#     #         WHERE username = %(username)s;
#     #         """,
#     #         {
#     #             "username": username
#     #         },
#     #     )
#     #     password_hash_from_db = cur.fetchone()[0]
#     #
#     #     auth_is_ok = pwd_context.verify(password, password_hash_from_db)
#     #     if auth_is_ok:
#     #         return jwt
#     #
#     #     return None
#
#
# def get_account_by_username(username: str) -> Optional[Account]:
#     app_logger.debug(f"getting account by username {username}")
#     with conn.cursor(row_factory=class_row(Account)) as cur:
#         cur.execute(
#             "SELECT * FROM accounts WHERE username = %(username)s;",
#             {"username": username},
#         )
#         account = cur.fetchone()
#
#         if not account:
#             # raise KeyError(f"User {username} not found")
#             return None
#
#         return account
#
#
# def get_account_by_id(account_id: UUID) -> Optional[Account]:
#     app_logger.debug(f"getting account by account_id {account_id}")
#     with conn.cursor(row_factory=class_row(Account)) as cur:
#         cur.execute(
#             "SELECT * FROM accounts WHERE id = %(account_id)s;",
#             {"account_id": account_id},
#         )
#         account = cur.fetchone()
#
#         if not account:
#             return None
#
#         return account
#
#
# def delete_account_by_id(account_id: UUID) -> bool:
#     app_logger.debug(f"deleting account by account_id {account_id}")
#     with conn.cursor() as cur:
#         cur.execute(
#             "DELETE FROM accounts WHERE id = %(account_id)s"
#             "RETURNING id;",
#             {"account_id": account_id},
#         )
#         conn.commit()
#
#         result = cur.fetchall()
#
#         if not result:
#             return False
#
#         return True
