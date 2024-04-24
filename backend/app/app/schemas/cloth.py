from enum import Enum
from odmantic import Field
from pydantic import BaseModel, AnyHttpUrl, Field


class ClothCatgeory(str, Enum):
    men = "men"
    women = "women"
    other = "other"


class ClothCreate(BaseModel):
    category: ClothCatgeory
    name: str = Field(..., min_length=1, max_length=100, examples=["T-shirt", "Shirt", "Pant", "Jeans"])
    price: float 
    image: str = Field(..., min_length=1, max_length=100, examples=["https://www.example.com/image.jpg"])


class ClothUpdate(BaseModel):
    category: ClothCatgeory
    name: str
    price: float

