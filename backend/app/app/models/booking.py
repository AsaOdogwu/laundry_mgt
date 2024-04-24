from app.db.base_class import Base
from odmantic import Field, EmbeddedModel
from enum import Enum
from typing import List
from datetime import datetime
from odmantic import ObjectId


class ClothCatgeory(str, Enum):
    men = "men"
    women = "women"
    other = "other"

class Clothes(EmbeddedModel):
    category: ClothCatgeory
    name: str
    quantity: int
    price: float


class Booking(Base):
    user_id: ObjectId
    total_quantity: int
    total_price: float
    address: str
    phone: str
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    clothes: List[Clothes]
