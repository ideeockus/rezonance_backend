from fastapi import APIRouter, HTTPException, status, Depends

from models.account import UserData, Contacts, Account
from models.dto.api.account import AccountDTO
from repositories import accounts_repository
from services.accounts_service.auth_token_utils import create_jwt_token, get_account_by_jwt_token

router = APIRouter(
    prefix="/api/users",
    tags=["account"],
)

# WARNING! put it to end of routes
# @router.get("/{username}", response_model=AccountDTO)
# async def get_user(username: str):
#     account = accounts_repository.get_account_by_username(username)
#
#     if not account:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#
#     return account


@router.post("/signup")
async def user_signup(username: str, password: str, user_data: UserData, contacts: Contacts):
    account_id = accounts_repository.create_account(username, password, user_data, contacts)
    if account_id is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
        # return None

    auth_token = create_jwt_token(username)

    return {"auth_token": auth_token}


@router.post("/signin")
async def user_signin(username: str, password: str):
    account = accounts_repository.get_account_by_credentials(username, password)
    if account is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        # return None

    auth_token = create_jwt_token(username)

    return {"auth_token": auth_token}


# def validate_token(token: str):
#     pass

@router.get("/me")
async def get_me(account: Account = Depends(get_account_by_jwt_token)):
    return AccountDTO(
        id=account.id,
        username=account.username,
        user_data=account.user_data,
    )


@router.get("/get_user")
async def get_user(username: str, account: Account = Depends(get_account_by_jwt_token)):
    user_account = accounts_repository.get_account_by_username(username)
    return AccountDTO(
        id=user_account.id,
        username=user_account.username,
        user_data=user_account.user_data,
    )


@router.get("/abc")
async def abc2():
    return {"abc": "123"}



