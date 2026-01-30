Python Flask App Deployment on Azure App Service

This repository contains my second hands-on Azure project, focused on understanding the Azure environment, governance, CI/CD, and deployment workflows as preparation for a cloud security career path.

The application itself is intentionally simple. The primary learning comes from deploying and operating it correctly in a real Azure environment.

Project Overview

Application: Simple Python web application using Flask

Cloud Platform: Microsoft Azure

Service: Azure App Service (Linux)

SKU / Plan: Basic B1

CI/CD: GitHub Actions

Runtime: Python 3.10

The objective of this project was to gain practical experience with:

Azure policy enforcement and governance

Application build vs runtime separation

CI/CD integration with Azure App Service

Debugging deployment and runtime issues using logs

Step 1: Writing a Simple Flask Application

app.py

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    env = os.getenv("ENV", "Not Set")
    version = os.getenv("APP_VERSION", "1.0")

    return f"""
    <h1>Hello from Azure App Service</h1>
    <p>ENV = {env}</p>
    <p>Version = {version}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


This application verifies:

Successful deployment

Runtime environment configuration through environment variables

Step 2: Dependencies

requirements.txt

flask
gunicorn


Flask is used as the web framework

Gunicorn is required as the production WSGI server for Azure App Service

Step 3: Azure Policy and Environment Constraints

During deployment, it became clear that Azure Student subscriptions enforce policies, including:

Deployment allowed only in specific regions

Policy evaluation occurring before resource creation

This reinforced the importance of understanding governance and policy controls, especially from a cloud security perspective.

Step 4: Azure App Service Configuration
Runtime

Operating System: Linux

Runtime Stack: Python 3.10

App Settings (Environment Variables)

Configured under Azure App Service → Environment variables:
<img width="1362" height="577" alt="Screenshot 2026-01-29 215637" src="https://github.com/user-attachments/assets/ad5e69d0-d35e-4e56-83ee-cc4487228d58" />



These settings ensure:

Consistent Python version for both build and runtime

Azure-managed dependency installation via Oryx

Secure and centralized configuration management

Step 5: Startup Command

Azure App Service does not use Flask’s development server.

The startup command configured in Azure:

gunicorn app:app


This explicitly defines how the application is started in production.

Step 6: CI/CD with GitHub Actions
<img width="801" height="213" alt="Screenshot 2026-01-29 214021" src="https://github.com/user-attachments/assets/dc7bc6d7-4d11-4335-b41d-2465e4adbb1e" />


The CI/CD pipeline is intentionally minimal and aligned with Azure’s build model.

.github/workflows/deploy.yml

name: Build and deploy Python app to Azure Web App - Python-App

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: python-app
          path: .

  deploy:
    runs-on: ubuntu-latest
    needs: build
    permissions:
      id-token: write
      contents: read

    steps:
      - uses: actions/download-artifact@v4
        with:
          name: python-app

      - uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZUREAPPSERVICE_CLIENTID }}
          tenant-id: ${{ secrets.AZUREAPPSERVICE_TENANTID }}
          subscription-id: ${{ secrets.AZUREAPPSERVICE_SUBSCRIPTIONID }}

      - uses: azure/webapps-deploy@v3
        with:
          app-name: Python-App

Design choices

Dependency installation handled by Azure (Oryx)

CI pipeline used strictly for delivery, not environment building

Reduced risk of Python version mismatch or misconfiguration

Step 7: Health Check Configuration

Azure App Service reports application health based on configured endpoints.
<img width="1362" height="577" alt="Screenshot 2026-01-29 215637" src="https://github.com/user-attachments/assets/9c57715e-7def-4510-863e-2e75442dd374" />


For this project:

Health Check path was set to /

This allowed Azure to verify the application was responding correctly

This step helped remove misleading “Issues Detected” warnings and reinforced the importance of explicit health signaling in production environments.

Step 8: Debugging and Verification

Primary debugging methods used:

GitHub Actions logs for workflow validation

Azure Log Stream for runtime and startup issues

Verification of environment variables and startup behavior

Issues addressed included:

Azure policy restrictions

Python version mismatches between build and runtime

CI/CD workflow syntax errors

Startup command misconfiguration

Environment variable propagation

Health check configuration

Azure App Service Plan (SKU: B1)

This project uses the Basic B1 App Service plan, which provides:

Dedicated compute resources

Sufficient CPU and memory for small production workloads

Better reliability than Free/Shared tiers

Support for features like Always On (optional)

Using B1 helped simulate a more realistic production setup compared to free tiers.

Final Result

The deployed application successfully displays:
<img width="1616" height="498" alt="Screenshot 2026-01-29 220125" src="https://github.com/user-attachments/assets/f7b8f2d5-4b4a-46c0-98ee-d226f3c3ec65" />
<img width="681" height="285" alt="Screenshot 2026-01-29 214453" src="https://github.com/user-attachments/assets/1f05527c-b6d3-4f4e-af14-4f774daa4daa" />


Key Learnings Relevant to Cloud Security

Azure policy enforcement and governance controls

Clear separation between build and runtime environments

Secure configuration using environment variables

CI/CD pipelines as a potential attack surface

Importance of logs over UI-based diagnostics

Health checks as part of application reliability and monitoring
