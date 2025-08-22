from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime  

class BrandBase(BaseModel):
    brand_name: str = Field(min_length=2, max_length=120)
    owner_name: str = Field(min_length=2, max_length=120)
    status: Optional[str] = "Pendiente"  

class BrandCreate(BrandBase):
    pass

class BrandUpdate(BaseModel):
    brand_name: Optional[str] = Field(default=None, min_length=2, max_length=120)
    owner_name: Optional[str] = Field(default=None, min_length=2, max_length=120)
    status: Optional[str] = Field(default=None)

class BrandOut(BrandBase):
    id: int
    created_at: Optional[datetime] = None   
    updated_at: Optional[datetime] = None  

    class Config:
        from_attributes = True
