from fastapi import Any,APIRouter,Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from motor.core import AgnosticDatabase

from app import crud,models
from app.api import deps
from app.core import security
from app.core.config import settings

router=APIRouter()

@router.post("/register/")
async def register_with_details(user,db: AgnosticDatabase = Depends(deps.get_db),form_data: OAuth2PasswordRequestForm=Depends()) -> Any:
    """
    First step with OAuth2 compatible token login, get an access token for checking if the user exists before registering user.
    """

    user = await crud.user.get_by_email (db,email=user.email)
    if user:
        return HTTPException(status_code=409,detail="User already exists,conflict in resolving")
    # Register user
    