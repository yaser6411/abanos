from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://abanos_user:V4lE2IwW152vA0c8JxnUMyA7HMp8OfnC@dpg-d90gp79o3t8c73c8d660-a.oregon-postgres.render.com/abanos"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
