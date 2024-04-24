from typing import Any, Dict, Optional, Type, Union
from xxlimited import Str

from bson import ObjectId
from motor.core import AgnosticDatabase

from app.crud.base import CRUDBase
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingUpdate


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):
    async def create_with_user_id(self, db: AgnosticDatabase, obj_in: BookingCreate, user_id:str) -> Booking:  # noqa        
        return await self.engine.save(Booking(**{**obj_in.model_dump(), "user_id": user_id}))

    # async def update(
    #     self,
    #     db: AgnosticDatabase,
    #     *,
    #     db_obj: Booking,
    #     obj_in: Union[ClothUpdate, Dict[str, Any]],
    # ) -> Cloth:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     return await self.engine.save(db_obj, **update_data)


booking = CRUDBooking(Booking)
