# Azure CI/CD Pipeline Project

## Overview

This project demonstrates a complete CI/CD (Continuous Integration and Continuous Deployment) pipeline using GitHub Actions, Docker Compose, and Microsoft Azure.

The pipeline automatically deploys application updates from GitHub to an Azure Linux Virtual Machine whenever code is pushed to the main branch.

This project was built to develop hands-on experience with cloud operations, DevOps practices, GitHub Actions, Linux administration, Docker containerization, SSH authentication, and automated deployments.

---

## Architecture

```text
Developer
    ↓
Git Push
    ↓
GitHub Repository
    ↓
GitHub Actions Workflow
    ↓
SSH Authentication
    ↓
Azure Linux Virtual Machine
    ↓
Docker Compose
    ↓
Flask Application
```

---

## Technologies Used

### Cloud

* Microsoft Azure
* Azure Linux Virtual Machine

### DevOps

* Git
* GitHub
* GitHub Actions
* Docker
* Docker Compose

### Linux

* Ubuntu Linux
* SSH
* System Administration

### Application

* Python
* Flask
* NGINX

---

## Features

* Source code hosted in GitHub
* Automated deployment pipeline using GitHub Actions
* Secure SSH authentication using deployment keys
* GitHub Secrets for credential management
* Docker containerized application deployment
* Docker Compose multi-service orchestration
* Automated application rebuild and redeployment
* Azure Linux VM hosting

---

## CI/CD Workflow

### Trigger

The deployment pipeline automatically runs when code is pushed to the main branch.

```yaml
on:
  push:
    branches:
      - main
```

### Deployment Process

1. Developer pushes code to GitHub
2. GitHub Actions workflow starts
3. GitHub authenticates using SSH deployment key
4. Workflow connects to Azure VM
5. Latest repository updates are pulled
6. Docker Compose rebuilds containers
7. Updated application is deployed automatically

---

## GitHub Secrets

The following repository secrets were configured:

* VM_HOST
* VM_USER
* VM_SSH_KEY

These secrets provide secure authentication without exposing credentials within the repository.

---

## Key Skills Demonstrated

* CI/CD Pipelines
* GitHub Actions
* Git Version Control
* Linux Administration
* SSH Authentication
* Docker
* Docker Compose
* Azure Virtual Machines
* Cloud Operations
* Infrastructure Automation
* DevOps Fundamentals
* Troubleshooting

---


## Future Improvements

* Automated testing before deployment
* Multi-environment deployments (Dev/Test/Production)
* Azure Container Registry (ACR)
* Azure App Service deployment
* Infrastructure provisioning with Terraform
* Kubernetes deployment with Azure Kubernetes Service (AKS)
* Monitoring and alerting integration

---

## Author

Jack Cundiff

Computer Science Student | AZ-900 Certified

Cloud Support • Cloud Operations • Cloud Engineering
