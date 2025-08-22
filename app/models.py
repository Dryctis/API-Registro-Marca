from sqlalchemy import Column, Integer, String, DateTime, func
from .db import Base

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(120), nullable=False, index=True)
    owner_name = Column(String(120), nullable=False, index=True)
    status = Column(String(20), nullable=False, default="Pendiente")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
