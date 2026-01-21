from app.quality_validator import validate_incident_quality
from app.validators.db_validator import validate_against_reference


def evaluate_incident_quality(incident: dict):
    # 1. Completeness (existing logic)
    base_result = validate_incident_quality(incident)

    # 2. Accuracy (DB validation)
    accuracy_errors = validate_against_reference(incident)
    accuracy_score = 100 if not accuracy_errors else max(50, 100 - len(accuracy_errors) * 25)

    # 3. Final score composition (Phase 1)
    final_score = int(
        base_result["quality_score"] * 0.6 +
        accuracy_score * 0.4
    )

    status = "GOOD" if final_score >= 70 else "POOR"

    return {
        "incident_number": incident["incident_number"],
        "quality_status": status,
        "quality_score": final_score,
        "missing_fields": base_result["missing_fields"],
        "accuracy_errors": accuracy_errors,
        "feedback": "AI-enhanced incident quality evaluation completed"
    }
