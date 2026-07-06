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

# User schemas
class UserCreate(BaseModel):
    full_name: str
    phone_number: str
    password: str

class UserOut(BaseModel):
    id: int
    full_name: str
    phone_number: str
    is_verified: bool
    class Config:
        orm_mode = True

# Auth token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    phone_number: Optional[str] = None
