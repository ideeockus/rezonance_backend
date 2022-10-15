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


class Contacts(BaseModel):
    email: str
    phone: str
    telegram: str
    instagram: str


class Account(BaseModel):
    id: int
    username: str
    user_data: UserData
    contacts: Contacts
