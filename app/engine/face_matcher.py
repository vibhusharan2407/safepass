from deepface import DeepFace
import os


def verify_faces(img1_path: str, img2_path: str):
    """
    Compares two images to check if they belong to the same person.
    Returns a dictionary with verified status and distance.
    """
    try:
        # DeepFace.verify returns a dict: {'verified': True/False, 'distance': 0.23, ...}
        # Model choices: "VGG-Face", "Facenet", "OpenFace". VGG-Face is the default and reliable.
        # enforce_detection=False allows the code to run even if it can't find a face in one image (prevents crashes)
        result = DeepFace.verify(
            img1_path=img1_path,
            img2_path=img2_path,
            model_name="VGG-Face",
            enforce_detection=False
        )

        return {
            "verified": result["verified"],
            "distance": round(result["distance"], 4),
            "error": None
        }

    except Exception as e:
        return {
            "verified": False,
            "distance": None,
            "error": str(e)
        }