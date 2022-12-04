from fastapi import APIRouter, HTTPException, status, Depends

from models.account import UserData, Contacts, Account
from models.dto.api.account import AccountDTO
from services.accounts_service import get_account_by_jwt_token

router = APIRouter(
    prefix="/api/events",
    tags=["event"],
)


@router.post("/create_event")
async def create_event(account: Account = Depends(get_account_by_jwt_token), event):
    account_id = accounts_repository.create_account(username, password, user_data, contacts)
    if account_id is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
        # return None

    auth_token = create_jwt_token(username)

    return {"auth_token": auth_token}


@router.get("/me")
async def get_me(account: Account = Depends(get_account_by_jwt_token)):
    return AccountDTO(
        id=account.id,
        username=account.username,
        user_data=account.user_data,
    )

# @router.get("/get_event")
# async def get_event(username: str, password: str):
#     account = accounts_repository.get_account_by_credentials(username, password)
#     if account is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
#         # return None
#
#     auth_token = create_jwt_token(username)
#
#     return {"auth_token": auth_token}




