from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..schemas import BrandCreate, BrandUpdate, BrandOut
from ..services.brands import BrandService

router = APIRouter(prefix="/api/brands", tags=["brands"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("", response_model=dict)
def list_brands(limit: int = 20, offset: int = 0, search: str | None = None, db: Session = Depends(get_db)):
    total, items = BrandService.list(db, limit, offset, search)
    return {"total": total, "items": [BrandOut.model_validate(i).model_dump() for i in items], "limit": limit, "offset": offset, "search": search}

@router.get("/{id}", response_model=BrandOut)
def get_brand(id: int, db: Session = Depends(get_db)):
    b = BrandService.get(db, id)
    if not b: raise HTTPException(404, "Not found")
    return b

@router.post("", response_model=BrandOut, status_code=201)
def create_brand(data: BrandCreate, db: Session = Depends(get_db)):
    return BrandService.create(db, data)

@router.put("/{id}", response_model=BrandOut)
def update_brand(id: int, data: BrandUpdate, db: Session = Depends(get_db)):
    b = BrandService.update(db, id, data)
    if not b: raise HTTPException(404, "Not found")
    return b

@router.delete("/{id}", status_code=204)
def delete_brand(id: int, db: Session = Depends(get_db)):
    ok = BrandService.delete(db, id)
    if not ok: raise HTTPException(404, "Not found")
    return
