#!/bin/bash

set -e

echo "🔹 Updating system..."
sudo apt update -y

echo "🔹 Installing core utilities..."
sudo apt install -y \
  curl \
  unzip \
  gnupg \
  lsb-release \
  ca-certificates \
  software-properties-common

echo "🔹 Installing Docker..."
if ! command -v docker &> /dev/null; then
  curl -fsSL https://get.docker.com | sudo sh
  sudo usermod -aG docker $USER
else
  echo "Docker already installed"
fi

echo "🔹 Installing Docker Compose plugin..."
sudo apt install -y docker-compose-plugin

echo "🔹 Installing Terraform..."
if ! command -v terraform &> /dev/null; then
  curl -fsSL https://releases.hashicorp.com/terraform/1.6.6/terraform_1.6.6_linux_amd64.zip -o terraform.zip
  unzip terraform.zip
  sudo mv terraform /usr/local/bin/
  rm terraform.zip
else
  echo "Terraform already installed"
fi

echo "🔹 Installing Python & venv..."
sudo apt install -y python3 python3-pip python3-venv

echo "✅ Setup completed. Restart your terminal before continuing."
