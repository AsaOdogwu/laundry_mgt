from fastapi import APIRouter, Depends, HTTPException
from motor.core import AgnosticDatabase

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.post("/booking")
async def book_laundry(
    *,
    db: AgnosticDatabase = Depends(deps.get_db),
    obj_in: schemas.BookingCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    booking = await crud.booking.create_with_user_id(db, obj_in=obj_in, user_id=current_user.id)
    return booking
