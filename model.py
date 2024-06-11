from pydantic import BaseModel


class Belgrade(BaseModel):
    Општина: str
    Време: str
    Улице: str


class Other_city(BaseModel):
    Огранак: str
    Општина: str
    Време: str
    Улице: str
