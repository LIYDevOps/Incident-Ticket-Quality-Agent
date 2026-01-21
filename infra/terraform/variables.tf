variable "container_name" {
  description = "Name of the backend container"
  type        = string
  default     = "incident-quality-backend"
}

variable "backend_port" {
  description = "Port on which FastAPI runs"
  type        = number
  default     = 8000
}
