MANDATORY_FIELDS = [
    "short_description",
    "description",
    "category",
    "priority",
    "assignment_group",
    "cmdb_ci"
]


def validate_incident_quality(incident: dict):
    missing_fields = []

    for field in MANDATORY_FIELDS:
        value = incident.get(field)
        if not value or not str(value).strip():
            missing_fields.append(field)

    if missing_fields:
        return {
            "quality_status": "POOR",
            "missing_fields": missing_fields,
            "message": "Incident is missing mandatory fields"
        }

    return {
        "quality_status": "GOOD",
        "missing_fields": [],
        "message": "Incident meets mandatory field requirements"
    }
