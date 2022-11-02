# from typing import Self
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserData(BaseModel):
    location: str  # ? city ?
    profession: Optional[str]
    headline: str
    about: Optional[str]
    targets: str
    first_name: str
    last_name: str

    lang: Optional[str]  # enum ?
    age: Optional[int]
    height: Optional[int]
    education: Optional[str]
    interests: Optional[str]
    hobby: Optional[str]
    music: Optional[str]
    sport: Optional[str]
    worldview: Optional[str]
    books: Optional[str]
    food: Optional[str]
    alcohol: Optional[bool]
    smoking: Optional[bool]

    @classmethod
    def mock(cls) -> "UserData":  # TODO replace with Self
        return cls(
            location="random_location", lang="ru", profession="programmer", headline="rezonance service backender",
            age=19, height=180, education="university", interests="random_interests", targets="random_targets",
            hobby="random_hobby", music="random_music", sport="ball sport", worldview="www", books="random_books",
            food="", alcohol=False, smoking=False, about="just working here", first_name="John", last_name="Doe",
        )


class Contacts(BaseModel):
    email: Optional[str]
    phone: Optional[str]
    telegram: Optional[str]
    instagram: Optional[str]

    @classmethod
    def mock(cls) -> "Contacts":
        return cls(
            email="random@example.com", phone="",
            telegram="",
        )


class Account(BaseModel):
    id: UUID
    username: str
    password_hash: str
    user_data: UserData
    contacts: Contacts
