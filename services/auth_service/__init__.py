from fastapi import APIRouter

from models.account import UserData, Contacts
from repositories.accounts import create_account

router = APIRouter()


@router.post("/api/user/signup")
async def user_signup(username: str, user_data: UserData, contacts: Contacts):
    account_id = create_account(username, user_data, contacts)
    if account_id is None:
        return None

    return account_id


@router.get("/api/")
async def abc2():
    return {"abc": "123"}
