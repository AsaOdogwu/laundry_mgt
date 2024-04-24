from datetime import datetime
from app.schemas.cloth import ClothCatgeory
from odmantic import Field
from enum import Enum
from pydantic import BaseModel, AnyHttpUrl, Field
from typing import List

class ClothCatgeory(str, Enum):
    men = "men"
    women = "women"
    other = "other"

class Clothes(BaseModel):
    category: ClothCatgeory = Field(..., min_length=1, max_length=100, examples=["men", "women", "other"])
    name: str = Field(..., min_length=1, max_length=100, examples=["T-shirt", "Shirt", "Pant", "Jeans"])
    quantity: int
    price: float
    
    
class BookingCreate(BaseModel):
    clothes: List[Clothes]
    address: str = Field(..., min_length=1, max_length=100, examples=["123, Example Street, Example City, Example Country"])
    instructions: str = Field(..., min_length=1, max_length=100, examples=["Please wash with care"])
    total_price: float = Field(..., examples=["1000"])
    phone: str
    total_quantity: int
    

class BookingUpdate(BaseModel):
    pass