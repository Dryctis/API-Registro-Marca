from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .db import Base, engine
from .models import *  

app = FastAPI(title="Brand Registry API", version="1.0.0")


origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]
origin_regex = getattr(settings, "CORS_ORIGIN_REGEX", None)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,                 
    allow_origin_regex=origin_regex,       
    allow_credentials=True,                
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=86400,                         
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

from .routers import health, brands 

app.include_router(health.router)
app.include_router(brands.router)

@app.get("/")
def root():
    return {"service": "brand-registry-api", "status": "ok"}
