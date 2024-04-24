from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from motor.core import AgnosticDatabase

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get("/cloth")
async def available_cloth(category: schemas.ClothCatgeory):
    return await crud.cloth.get_by_category(category)


@router.post("/cloth")
async def create_cloth(
    *,
    db: AgnosticDatabase = Depends(deps.get_db),
    obj_in: schemas.ClothCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new cloth.
    """
    cloth = await crud.cloth.create(db, obj_in=obj_in)
    return cloth