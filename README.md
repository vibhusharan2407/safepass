# SafePass: Identity Verification Microservice 🛡️

SafePass is a robust KYC (Know Your Customer) API built to verify user identities automatically. It utilizes **Deep Learning (DeepFace)** to perform facial recognition between a user's ID card and a live selfie, logging all attempts into a **PostgreSQL** database for audit trails.

## 🚀 Tech Stack
* **Backend:** Python 3.9, FastAPI
* **AI/ML:** DeepFace, TensorFlow, Keras (VGG-Face Model)
* **Database:** PostgreSQL, SQLAlchemy
* **Infrastructure:** Docker & Docker Compose

## ⚡ Features
* **Face Matching:** Compares ID card photo vs. Selfie with high accuracy.
* **Audit Logging:** Automatically saves verification results (Approved/Rejected) and confidence scores to the database.
* **Dockerized:** One-command setup for the entire stack.

## 🛠️ How to Run
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/vibhusharan2407/safepass.git](https://github.com/vibhusharan2407/safepass.git)
    cd safepass
    ```
2.  **Start the stack:**
    ```bash
    docker compose up --build
    ```
3.  **Test the API:**
    Open `http://localhost:8000/docs` and try the `POST /api/v1/verify` endpoint.
