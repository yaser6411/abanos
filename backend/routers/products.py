from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from backend import crud, schemas
from backend.database import get_db

router = APIRouter()

@router.get("/products", response_model=List[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.post("/products", response_model=schemas.ProductOut)
def create_product(product_in: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product_in)

@router.get("/vendors", response_model=List[schemas.VendorOut])
def list_vendors(db: Session = Depends(get_db)):
    return crud.get_vendors(db)

@router.post("/vendors", response_model=schemas.VendorOut)
def create_vendor(vendor_in: schemas.VendorCreate, db: Session = Depends(get_db)):
    return crud.create_vendor(db, vendor_in)
