from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.seed import seed_data
from app.quality_engine import evaluate_incident_quality

from app.schemas import IncidentPayload
from app.quality_validator import validate_incident_quality

app = FastAPI(
    title="Incident Quality Analysis Agent",
    version="1.0.0"
)

# Template configuration
templates = Jinja2Templates(directory="templates")


@app.get("/health")
def health():
    return {"status": "UP"}

@app.post("/analyze-incident")
def analyze_incident(payload: IncidentPayload):
    return evaluate_incident_quality(payload.dict())

@app.post("/analyze-incident")
def analyze_incident(payload: IncidentPayload):
    """
    API endpoint used by ServiceNow / UI
    """
    result = evaluate_incident_quality(payload.dict())

    return {
        "incident_number": payload.incident_number,
        "quality_status": result["quality_status"],
        "quality_score": result["quality_score"],
        "missing_fields": result["missing_fields"],
        "feedback": result["message"]
    }


@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    """
    Mock ServiceNow UI using FastAPI
    """
    return templates.TemplateResponse(
        "incident_ui.html",
        {"request": request}
    )

@app.on_event("startup")
def startup_event():
    seed_data()