from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine, Base
import backend.models  # ensure models are imported so SQLAlchemy sees them
from backend.routers import products_router, auth_router

app = FastAPI(title="Abanos API")

# Development CORS policy; tighten for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"status": "OK", "project": "Abanos"}

@app.get("/db-check")
def db_check():
    try:
        conn = engine.connect()
        conn.close()
        return {"database": "connected successfully"}
    except Exception as e:
        return {"database": "failed", "error": str(e)}

# API routers
app.include_router(products_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")
