from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, HTTPException, status, Depends

from models.account import Account
from models.event import EventType
from models.other import Location
from repositories import events_repository
from services.accounts_service import get_account_by_jwt_token

router = APIRouter(
    prefix="/api/events",
    tags=["event"],
)


@router.post("/create_event")
async def create_event(event_name: str, description: str, date: datetime, event_type: EventType, location: Location,
                       account: Account = Depends(get_account_by_jwt_token)):
    event_id = events_repository.create_event(event_name, description, date, account.id, event_type, location)
    if event_id is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    # add current user to participants

    return {"event_id": event_id}


@router.get("/get_event")
async def get_event(event_id: UUID,
                    account: Account = Depends(get_account_by_jwt_token)):
    if account is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    event = events_repository.get_event_by_id(event_id)
    if event is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"event": event}




