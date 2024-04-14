from pydantic import BaseModel,Field
from typing import Optional


class TypeOfCloth(BaseModel):
    jeans: int
    senator_wears: int
    suede: int
    shirt:int
    top: int
    singlet:int
    plain_trouser:int
    jersey: int
    duvet: int
    bedcover: int
    pillowcover:int
    others: int= Field(description="Any other kind of material not included")




class BookingCreate(BaseModel):
    pickup_date: str
    delivery_date: str
    gender:str
    status:str= Field(description=["pending","completed","cancelled"])
    total_amount: float
    type_of_cloth:TypeOfCloth = Optional [int] | 0












