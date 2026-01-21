MANDATORY_FIELDS = [
    "short_description",
    "description",
    "category",
    "priority",
    "assignment_group",
    "cmdb_ci"
]

TOTAL_FIELDS = len(MANDATORY_FIELDS)


def validate_incident_quality(incident: dict):
    """
    Validates incident quality based on mandatory fields
    and returns quality score + status.
    """

    missing_fields = []

    for field in MANDATORY_FIELDS:
        value = incident.get(field)
        if not value or not str(value).strip():
            missing_fields.append(field)

    filled_fields = TOTAL_FIELDS - len(missing_fields)
    quality_score = int((filled_fields / TOTAL_FIELDS) * 100)

    quality_status = "GOOD" if quality_score >= 70 else "POOR"

    message = (
        "Incident meets quality standards"
        if quality_status == "GOOD"
        else "Incident is missing mandatory fields"
    )

    return {
        "quality_status": quality_status,
        "quality_score": quality_score,
        "missing_fields": missing_fields,
        "message": message
    }
