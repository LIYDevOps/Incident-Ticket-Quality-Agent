### Project Use Case ###
The Incident Quality Analysis Agent is an enterprise‑grade ServiceNow implementation that focuses on improving the quality of incident data at the time of Incident creation.

This project addresses that problem by introducing a custom ServiceNow Incident Page that validates incident data and integrates with an external AI-ready API for quality analysis.

## Architecture Overview ##

Service Portal Page (UI)
↓
Service Portal Widget
↓
Client Controller (AngularJS)
↓
Widget Server Script
↓
Script Include (Business Logic)
↓
RESTMessageV2 (Integration Layer)
↓
External API (FastAPI – AI Ready)

## Technology Stack ##

Frontedn + Backend
Service Portal – Custom page
Service Portal Widget – Incident form
AngularJS – Client-side controller
Script Include – Server-side business logic
RESTMessageV2 – Secure outbound integration

External Backend
Python FastAPI - API endpoint
JSON Schema - Payload validation

User Flow
1. User opens Incident Quality Portal Page
2. Fills incident details
3. Clicks Submit / Analyze Incident
4. Client-side validation runs
5. Incident is created server-side
6. Data sent to external API
7. Quality feedback returned
8. Message displayed to user / comment added

