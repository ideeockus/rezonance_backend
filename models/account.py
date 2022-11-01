# from typing import Self
from uuid import UUID

from pydantic import BaseModel


class UserData(BaseModel):
    location: str  # ? city ?
    lang: str  # enum ?
    profession: str
    work: str
    age: int
    height: int
    education: str
    interests: str
    life_targets: str
    hobby: str
    music: str
    sport: str
    worldview: str
    books: str
    food: str
    alcohol: bool
    smoking: bool

    @classmethod
    def mock(cls) -> "UserData":  # TODO replace with Self
        return cls(
            location="random_location", lang="ru", profession="programmer", work="rezonance_service", age=19,
            height=180, education="university", interests="random_interests", life_targets="random_targets",
            hobby="random_hobby", music="random_music", sport="ball sport", worldview="www", books="random_books",
            food="", alcohol=False, smoking=False
        )


class Contacts(BaseModel):
    email: str
    phone: str
    telegram: str
    instagram: str

    @classmethod
    def mock(cls) -> "Contacts":
        return cls(
            email="random@example.com", phone="",
            telegram="", instagram=""
        )


class Account(BaseModel):
    id: UUID
    username: str
    password_hash: str
    user_data: UserData
    contacts: Contacts
