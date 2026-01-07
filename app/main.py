from fastapi import FastAPI
from app.api import auth, pos, dashboard, ai
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tukey Decision Intelligence API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(pos.router, prefix="/pos", tags=["POS"])
app.include_router(dashboard.router, prefix="/dashboards", tags=["Dashboards"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])

@app.get("/health")
def health():
    return {"status": "ok"}




