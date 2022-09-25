from pydantic import BaseModel


class ServiceData(BaseModel):
    location: str  # ? city ?
    lang: str  # enum ?
    profession: str
    work: str
    age: int
    height: int
    education: str
    interests: str
    life_targets: str
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


class Person(BaseModel):
    id: int
    username: str
    service_data: ServiceData
    contacts: Contacts
