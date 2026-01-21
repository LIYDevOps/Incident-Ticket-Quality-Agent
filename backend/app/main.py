from fastapi import FastAPI
from app.schemas import IncidentPayload
from app.quality_validator import validate_incident_quality

app = FastAPI(
    title="Incident Quality Analysis Agent",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "UP"}


@app.post("/analyze-incident")
def analyze_incident(payload: IncidentPayload):
    result = validate_incident_quality(payload.dict())

    response = {
        "incident_number": payload.incident_number,
        "quality_status": result["quality_status"],
        "missing_fields": result["missing_fields"],
        "feedback": result["message"]
    }

    return response
