from datetime import datetime
from enum import Enum, auto
from typing import List
from uuid import UUID

from pydantic import BaseModel

from models.other import Location


class EventType(Enum):
    P2P = auto()
    OFFLINE_MEETUP = auto()
    ONLINE = auto()


class Event(BaseModel):
    id: UUID
    name: str
    description: str
    date: datetime
    participants: List[UUID]  # accounts ids
    type: EventType
    location: Location
