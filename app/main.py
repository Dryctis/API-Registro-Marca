from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .db import Base, engine
from .models import *  # noqa

app = FastAPI(title="Brand Registry API", version="1.0.0")

# --- CORS robusto ---
raw = (settings.CORS_ORIGINS or "").strip()
if raw == "*" or raw == "":
    allow_origins = ["*"]
    allow_credentials = False  # "*" + credentials no es válido; lo forzamos a False
    allow_origin_regex = None
else:
    allow_origins = [o.strip() for o in raw.split(",") if o.strip()]
    allow_credentials = True
    # Si algún día agregas este campo en config, lo usamos; si no, None
    allow_origin_regex = getattr(settings, "CORS_ORIGIN_REGEX", None) or None

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_origin_regex=allow_origin_regex,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=86400,
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

from .routers import health, brands  # noqa

app.include_router(health.router)
app.include_router(brands.router)

@app.get("/")
def root():
    return {"service": "brand-registry-api", "status": "ok"}
