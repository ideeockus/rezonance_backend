from datetime import datetime
from enum import Enum, auto
from typing import List
from uuid import UUID

from pydantic import BaseModel

from models.other import Location


class EventType(Enum):
    P2P = "P2P"
    OFFLINE_MEETUP = "OFFLINE_MEETUP"
    ONLINE = "ONLINE"


class Event(BaseModel):
    id: UUID
    name: str
    description: str
    date: datetime
    owner_id: UUID
    # participants: List[UUID]  # accounts ids
    type: EventType
    location: Location
