from typing import Any, Dict, Optional, Type, Union

from motor.core import AgnosticDatabase

from app.crud.base import CRUDBase
from app.models.cloth import Cloth
from app.schemas.cloth import ClothCreate, ClothUpdate


class CRUDCloth(CRUDBase[Cloth, ClothCreate, ClothUpdate]):
    
    def __init__(self, Model):
        super().__init__(Model)
        self.configure(Model)
        
    async def configure(self, Model):
        print("got here")
        await self.engine.configure_database([Model])

    async def get_by_category(self, category: str):
        return await self.engine.find(Cloth, Cloth.category == category)
    
    async def create(self, db: AgnosticDatabase, *, obj_in: ClothCreate) -> Cloth: # noqa
        return await self.engine.save(Cloth(**obj_in.model_dump()))

    
    async def update(
        self,
        db: AgnosticDatabase,
        *,
        db_obj: Cloth,
        obj_in: Union[ClothUpdate, Dict[str, Any]]
    ) -> Cloth:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return await self.engine.save(db_obj, **update_data)



cloth = CRUDCloth(Cloth)