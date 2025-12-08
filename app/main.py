from fastapi import FastAPI
from app.api.v1 import kyc
from app.core.database import engine
from app.models import verification

# Create the tables in the database
verification.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SafePass Identity Verification")

app.include_router(kyc.router, prefix="/api/v1", tags=["KYC"])

@app.get("/")
def root():
    return {"message": "SafePass API is running and connected to DB"}