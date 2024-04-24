from app.db.base_class import Base
from odmantic import Field

from pydantic import AnyHttpUrl


class Cloth(Base):
    category: str
    name: str = Field(unique=True)
    price: float
    image: str
