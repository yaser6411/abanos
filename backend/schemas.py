from pydantic import BaseModel
from typing import Optional

class VendorBase(BaseModel):
    name: str
    description: Optional[str] = None

class VendorCreate(VendorBase):
    pass

class VendorOut(VendorBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    vendor_id: Optional[int] = None

class ProductOut(ProductBase):
    id: int
    vendor: Optional[VendorOut] = None
    class Config:
        orm_mode = True
