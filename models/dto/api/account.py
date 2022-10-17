from uuid import UUID

from pydantic import BaseModel

from models.account import UserData


class AccountDTO(BaseModel):
    id: UUID
    username: str
    user_data: UserData
