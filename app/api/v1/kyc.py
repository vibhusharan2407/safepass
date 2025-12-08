from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from app.engine.face_matcher import verify_faces
from app.core.database import get_db
from app.models.verification import VerificationRequest
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/verify")
async def verify_identity(
        id_card: UploadFile = File(...),
        selfie: UploadFile = File(...)
        , db: Session = Depends(get_db)  # Inject Database Session
):
    # 1. Validation & Saving Files
    valid_extensions = ["image/jpeg", "image/png", "image/jpg"]
    if id_card.content_type not in valid_extensions:
        raise HTTPException(status_code=400, detail="Invalid ID Card format")
    if selfie.content_type not in valid_extensions:
        raise HTTPException(status_code=400, detail="Invalid Selfie format")

    id_card_path = os.path.join(UPLOAD_DIR, f"id_{id_card.filename}")
    selfie_path = os.path.join(UPLOAD_DIR, f"selfie_{selfie.filename}")

    with open(id_card_path, "wb") as buffer:
        shutil.copyfileobj(id_card.file, buffer)
    with open(selfie_path, "wb") as buffer:
        shutil.copyfileobj(selfie.file, buffer)

    # 2. Run AI Engine
    result = verify_faces(id_card_path, selfie_path)

    # 3. Save to Database (The Resume Booster Step)
    is_match = result["verified"]
    db_record = VerificationRequest(
        id_card_filename=id_card.filename,
        selfie_filename=selfie.filename,
        is_verified=is_match,
        distance_score=result["distance"],
        model_used="VGG-Face",
        status="APPROVED" if is_match else "REJECTED"
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return {
        "status": "completed",
        "verification_id": db_record.id,  # Return the DB ID
        "outcome": db_record.status,
        "confidence_score": db_record.distance_score
    }