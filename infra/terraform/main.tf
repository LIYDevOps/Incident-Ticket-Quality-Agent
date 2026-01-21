provider "docker" {}

# Build Docker Image
resource "docker_image" "backend" {
  name = "incident-quality-backend:latest"

  build {
    context    = "../../backend"
    dockerfile = "Dockerfile"
  }
}

# Run Container
resource "docker_container" "backend" {
  name  = var.container_name
  image = docker_image.backend.name

  ports {
    internal = var.backend_port
    external = var.backend_port
  }

  env = [
    "APP_ENV=dev"
  ]

  restart = "unless-stopped"
}
