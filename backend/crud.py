from sqlalchemy.orm import Session
import backend.models as models
import backend.schemas as schemas

def get_products(db: Session, limit: int = 100):
    return db.query(models.Product).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        vendor_id=product.vendor_id if product.vendor_id else None
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_vendors(db: Session, limit: int = 100):
    return db.query(models.Vendor).limit(limit).all()

def create_vendor(db: Session, vendor: schemas.VendorCreate):
    db_vendor = models.Vendor(name=vendor.name, description=vendor.description)
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor
