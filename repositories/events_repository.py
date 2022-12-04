from datetime import datetime
from typing import Optional, List
from uuid import UUID

import psycopg
from psycopg.rows import class_row

from configuration import ServiceConfig, app_logger
from models.event import Event, EventType
from models.other import Location

conn = psycopg.connect(
    ServiceConfig.POSTGRES_DB_URL,
)


def create_event(event_name: str, description: str, date: datetime, owner_id: UUID, event_type: EventType,
                 location: Location) -> Optional[UUID]:
    app_logger.debug(f"creating event {event_name}")

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO events (name, description, date, owner_id, type, location)
                VALUES (%(name)s, %(description)s, %(date)s, %(owner_id)s, %(event_type)s, %(location)s)
                RETURNING id;
                """,
                {
                    "name": event_name,
                    "description": description,
                    "date": date,
                    "owner_id": owner_id,
                    "event_type": event_type,
                    "location": location.json(),
                },
            )
            event_id = cur.fetchone()[0]

            conn.commit()
            return event_id
    except psycopg.errors.Error as e:
        app_logger.exception(f"error: {e}")
        conn.rollback()  # need to rollback in case of exception
        return None


def get_event_by_id(event_id: UUID) -> Optional[Event]:
    app_logger.debug(f"getting event by event_id {event_id}")
    with conn.cursor(row_factory=class_row(Event)) as cur:
        cur.execute(
            "SELECT * FROM events WHERE id = %(event_id)s;",
            {"event_id": event_id},
        )
        event = cur.fetchone()

        if not event:
            return None

        return event


# def get_participants_ids_by_event_id(event_id: UUID) -> Optional[List[UUID]]:
#     app_logger.debug(f"getting event by event_id {event_id}")
#     with conn.cursor(row_factory=class_row(Event)) as cur:
#         cur.execute(
#             "SELECT "
#             "SELECT * FROM events WHERE id = %(event_id)s;",
#             {"event_id": event_id},
#         )
#         event = cur.fetchone()
#
#         if not event:
#             return None
#
#         return event


def delete_event_by_id(event_id: UUID) -> bool:
    app_logger.debug(f"deleting event by event_id {event_id}")
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM events WHERE id = %(event_id)s"
            "RETURNING id;",
            {"event_id": event_id},
        )
        conn.commit()

        result = cur.fetchall()

        if not result:
            return False

        return True
