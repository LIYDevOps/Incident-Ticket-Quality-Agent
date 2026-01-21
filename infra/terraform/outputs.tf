output "backend_url" {
  description = "FastAPI backend URL"
  value       = "http://localhost:${var.backend_port}"
}
