from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class VerificationRequest(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Files
    id_card_filename = Column(String)
    selfie_filename = Column(String)

    # AI Results
    is_verified = Column(Boolean)
    distance_score = Column(Float)  # Lower is better (0.0 means identical)
    model_used = Column(String)  # e.g., "VGG-Face"

    # Metadata
    status = Column(String)  # "APPROVED" or "REJECTED"