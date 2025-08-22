from sqlalchemy.orm import Session
from sqlalchemy import or_, select, func  
from ..models import Brand

class BrandRepo:
    @staticmethod
    def create(db: Session, brand_name: str, owner_name: str, status: str = "Pendiente") -> Brand:
        b = Brand(brand_name=brand_name, owner_name=owner_name, status=status or "Pendiente")
        db.add(b)
        db.commit()
        db.refresh(b)
        return b

    @staticmethod
    def get(db: Session, id: int) -> Brand | None:
        return db.get(Brand, id)

    @staticmethod
    def list(db: Session, limit: int, offset: int, search: str | None):
        stmt = select(Brand)
        if search:
            s = f"%{search}%"
            stmt = stmt.where(or_(Brand.brand_name.ilike(s), Brand.owner_name.ilike(s)))

        
        total_stmt = select(func.count()).select_from(stmt.subquery())
        total = db.scalar(total_stmt)

        
        stmt = stmt.order_by(Brand.id.asc()).offset(offset).limit(limit)
        items = db.execute(stmt).scalars().all()
        return total, items

    @staticmethod
    def update(db: Session, id: int, **patch) -> Brand | None:
        b = db.get(Brand, id)
        if not b:
            return None
        for k, v in patch.items():
            if v is not None:
                setattr(b, k, v)
        db.commit()
        db.refresh(b)
        return b

    @staticmethod
    def delete(db: Session, id: int) -> bool:
        b = db.get(Brand, id)
        if not b:
            return False
        db.delete(b)
        db.commit()
        return True
