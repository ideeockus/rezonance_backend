from fastapi import APIRouter, HTTPException, status, Depends

from models.account import UserData, Contacts, Account
from models.dto.api.account import AccountDTO
from repositories import accounts_repository

router = APIRouter(
    prefix="/api/users",
    tags=["account"],
)


@router.get("/{username}", response_model=AccountDTO)
async def get_user(username: str):
    account = accounts_repository.get_account_by_username(username)

    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return account


@router.post("/signup")
async def user_signup(username: str, user_data: UserData, contacts: Contacts):
    account_id = accounts_repository.create_account(username, user_data, contacts)
    if account_id is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
        # return None

    return account_id


def validate_token(token: str):
    pass


@router.get("/me")
async def get_me(account: Account = Depends(validate_token)):
    pass


@router.get("/abc")
async def abc2():
    return {"abc": "123"}
