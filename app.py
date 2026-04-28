from fastapi import FastAPI
from pydantic import BaseModel
import logging

# ML classifier import
from ml_classifier import classify_email_ml

# Response generator import
from response_generator import generate_response

# FastAPI app
app = FastAPI(
    title="AI Workflow API",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Input schema
class EmailInput(BaseModel):
    email: str

# API endpoint
@app.post("/process-email")
def process_email(data: EmailInput):
    try:
        logging.info(f"Received email: {data.email}")

        # Empty input check
        if not data.email.strip():
            return {"error": "Email cannot be empty"}

        # ML classification
        category = classify_email_ml(data.email)
        logging.info(f"Category predicted: {category}")

        # Priority logic
        if category == "Complaint":
            priority = "High"
        elif category == "Inquiry":
            priority = "Medium"
        else:
            priority = "Low"

        # Generate response
        response = generate_response(category)

        # Final output
        return {
            "category": category,
            "priority": priority,
            "response": response
        }

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}