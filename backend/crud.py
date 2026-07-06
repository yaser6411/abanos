from sqlalchemy.orm import Session
import backend.models as models
import backend.schemas as schemas

# Product/vendor functions
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

# User functions
def get_user_by_phone(db: Session, phone_number: str):
    return db.query(models.User).filter(models.User.phone_number == phone_number).first()

def create_user(db: Session, full_name: str, phone_number: str, password_hash: str):
    db_user = models.User(full_name=full_name, phone_number=phone_number, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
