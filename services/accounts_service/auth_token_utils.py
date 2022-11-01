from datetime import datetime, timedelta

from jose import jwt, JWTError
from fastapi import status, HTTPException

from configuration import ServiceConfig, app_logger
from models.account import Account
from repositories import accounts_repository


def create_jwt_token(username: str):
    expiration_date = datetime.now() + timedelta(days=1)
    to_encode = {
        "sub": username,
        "exp": expiration_date
    }

    encoded_jwt = jwt.encode(to_encode, ServiceConfig.SECRET_KEY, algorithm=ServiceConfig.JWT_ALGORITHM)
    return encoded_jwt


def get_account_by_jwt_token(token: str) -> Account:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, ServiceConfig.SECRET_KEY, algorithms=[ServiceConfig.JWT_ALGORITHM])
        # app_logger.debug(f"payload: {payload}")
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    account = accounts_repository.get_account_by_username(username)
    if account is None:
        raise credentials_exception
    return account
