from typing import Any,Dict, Optional,Union

from motor.core import AgnosticDatabase

from app.core.security import get_password_hash, get_bookings,verify_password
from app.crud.base import CRUDBase,user
from app.models.bookings import Bookings
from app.schemas.bookings import BookingCreate


class CRUDBookings(CRUDBase[Bookings,BookingCreate]):
       async def get_bookings(self,db:AgnosticDatabase,*,email:str) -> Optional[BookingCreate]:
              return await self.engine.find_one(BookingCreate,BookingCreate.email == email)
async def create_booking(self,db:AgnosticDatabase,*,obj_in:BookingCreate) -> Bookings:
        bookings = {
            **obj_in.model_dump(),
            "email": obj_in.email,
            "hashed_password": get_password_hash(obj_in.password) if obj_in.password is not None else None,
            "full_name": obj_in.full_name,
            "email":obj_in.email,
            "type_of_cloth": obj_in.TypeOfCloth,
            
        }
        return await self.engine.save(Bookings(**bookings))

async def update(self,db: AgnosticDatabase, *,db_obj:Bookings,obj_in:Union[Bookings,Dict[str,Any]])-> Bookings:
        if isinstance(obj_in,dict):
                update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if update_data.get("bookings"):
            get_bookings = Bookings(update_data["bookings"])
            del update_data["bookings"]
            update_data[BookingCreate]
        if update_data.get("BookingCreate") and db_obj.delivery_date != update_data["bookings"]:
               update_data["bookings_validated"] = False
               return await user().update(db,db_obj=db_obj,obj_in=update_data)
def delete_booking(self, pickup_date: str) -> Optional[BookingCreate]:
    for i, booking in enumerate(self.bookings):
        if booking.pickup_date == pickup_date:
            return self.bookings.pop(i)
    return None
        
         
bookings = CRUDBookings(BookingCreate)     

#######gpt#####

from typing import Any, Dict, Optional, Union

from motor.core import AgnosticDatabase

from app.core.security import get_password_hash
from app.crud.base import CRUDBase
from app.models.bookings import Bookings
from app.schemas.bookings import BookingCreate


class CRUDBookings(CRUDBase[Bookings, BookingCreate]):
    async def get_booking_by_email(self, db: AgnosticDatabase, *, email: str) -> Optional[Bookings]:
        return await self.find_one(db, {"email": email})

    async def create_booking(self, db: AgnosticDatabase, *, obj_in: BookingCreate) -> Bookings:
        bookings_data = obj_in.dict()
        hashed_password = get_password_hash(obj_in.password) if obj_in.password else None
        bookings_data.update({"hashed_password": hashed_password})
        return await self.create(db, obj_in=bookings_data)

    async def update_booking(self, db: AgnosticDatabase, *, db_obj: Bookings, obj_in: Union[Bookings, Dict[str, Any]]) -> Bookings:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        if "bookings" in update_data:
            del update_data["bookings"]

        if "delivery_date" in update_data and db_obj.delivery_date != update_data["delivery_date"]:
            update_data["bookings_validated"] = False

        return await self.update(db, db_obj=db_obj, obj_in=update_data)


bookings = CRUDBookings(Bookings, BookingCreate)

