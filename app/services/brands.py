from sqlalchemy.orm import Session
from ..repos.brands import BrandRepo
from ..schemas import BrandCreate, BrandUpdate
from ..models import Brand

class BrandService:
    @staticmethod
    def create(db: Session, data: BrandCreate) -> Brand:
        return BrandRepo.create(db, data.brand_name, data.owner_name, data.status or "Pendiente")

    @staticmethod
    def get(db: Session, id: int) -> Brand | None:
        return BrandRepo.get(db, id)

    @staticmethod
    def list(db: Session, limit: int, offset: int, search: str | None):
        limit = max(1, min(100, int(limit)))
        offset = max(0, int(offset))
        return BrandRepo.list(db, limit, offset, search)

    @staticmethod
    def update(db: Session, id: int, data: BrandUpdate) -> Brand | None:
        return BrandRepo.update(db, id, **data.model_dump(exclude_unset=True))

    @staticmethod
    def delete(db: Session, id: int) -> bool:
        return BrandRepo.delete(db, id)
