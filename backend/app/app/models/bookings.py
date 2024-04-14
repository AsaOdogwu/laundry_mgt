from pydantic import Base, Field
from datetime import datetime

class Bookings(Base):
    pickup_date: str
    delivery_date: datetime
    gender:str
    status:str= Field(description=["pending","completed","cancelled"])
    total_amount: float


class TypeOfCloth(Base):
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