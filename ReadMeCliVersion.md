# Azure Flask Deployment – App Service Setup (CLI)
**Before starting I had already created a resource group where all the resources were made under**
## Step 1: Create an App Service Plan 
**Command:**
`az>> appservice plan create  --name flask-cli --resource-group Static_WebCLI  --location koreacentral --sku B1 --is-linux` 
Creates a Linux-based App Service Plan that defines the compute resources (CPU, memory, pricing tier) used by your Flask web app.

`appservice plan create`
Creates a new App Service Plan, which is the hosting container for one or more web apps.
`--name flask-cli`: Sets the name of the App Service Plan (this is not the web app name).
`--resource-group Static_WebCLI`: Specifies the resource group where the plan will live.
`--location koreacentral`: Chooses the Azure region where the infrastructure is deployed.
`--sku B1`:Selects the pricing tier (B1 = Basic tier, paid, supports custom startup commands).
`--is-linux`: Forces the plan to run on Linux (required for most Python/Flask deployments).

<img width="1677" height="857" alt="Screenshot 2026-02-07 110705" src="https://github.com/user-attachments/assets/849d9427-0cb4-4cef-955d-1af9126db7fd" />
<img width="1798" height="116" alt="Screenshot 2026-02-07 111716" src="https://github.com/user-attachments/assets/60593687-860b-4490-97d5-fe606b675c2d" />


## Step 2: Configure Flask App Startup Command
**Command:**
`az>> webapp config set --resource-group Static_WebCLI --name Flask-App--CLI  --startup-file "gunicorn app:app"`
Configures how Azure starts your Flask application by defining the command used to launch the web server.

`webapp config set`
Updates runtime configuration settings for an existing Azure Web App.
`--resource-group Static_WebCLI`: Identifies the resource group containing the web app. 
`--name Flask-App--CLI`: Specifies the exact name of the Azure Web App being configured.
`--startup-file "gunicorn app:app"`: Tells Azure to start the app using Gunicorn loading the Flask instance named app from app.py.
<img width="1326" height="626" alt="Screenshot 2026-02-07 193646" src="https://github.com/user-attachments/assets/20ccf8be-f0b8-45c8-83b4-3485c29ccc5a" />

## Step 3: Set App Settings
**Command:**
`az>> webapp config appsettings set --resource-group Static_WebCLI --name Flask-App--CLI --settings PYTHON_VERSION=3.10 SCM_DO_BUILD_DURING_DEPLOYMENT=true ENV=PRODUCTION APP_VERSION=1.0.0`
Sets application-level environment variables for the Azure Web App. These settings control the Python runtime, deployment behavior, and runtime environment configuration.

`webapp config appsettings set`  
Creates or updates environment variables (App Settings) for an Azure Web App.
`--resource-group Static_WebCLI`: Specifies the resource group containing the web app.
`--name Flask-App--CLI`: Identifies the target Azure Web App.
`--settings`: Defines key-value pairs that will be injected as environment variables at runtime.
**Configured Settings:**
`PYTHON_VERSION=3.10`: Specifies the Python runtime version used by the application.
`SCM_DO_BUILD_DURING_DEPLOYMENT=true`: Forces Azure to install dependencies and run build steps during deployment.
ENV=PRODUCTION`: Indicates the application is running in a production environment.
`APP_VERSION=1.0.0`: Custom version identifier for tracking application releases.
<img width="1870" height="574" alt="Screenshot 2026-02-07 225617" src="https://github.com/user-attachments/assets/05dc6b0d-052e-4a55-a9a0-50a6e6031ae5" />

## Step 4: Enable Application Logs
**Command:**
`az>> webapp log config --name Flask-App--CLI --resource-group Static_WebCLI --application-logging filesystem --level information`
Streams live application logs to the terminal, useful for debugging startup issues, deployment failures, or runtime errors.

`az webapp log tail`  
Connects to the web app log stream and outputs logs in real time.
`--name Flask-App--CLI`: Target web app.
`--resource-group Static_WebCLI`: Resource group containing the web app.
<img width="1795" height="972" alt="Screenshot 2026-02-07 230216" src="https://github.com/user-attachments/assets/e29f3cfd-76aa-4eec-9df6-67491b6f3096" />

## Step 5: Connect GitHub Repo
**Command:**
`az>> webapp deployment source config --name Flask-App--CLI --resource-group Static_WebCLI  --repo-url "https://github.com/akashn-oss/Azure-Building-a-Python-Web-Application.git" --branch "main" --manual-integration`
Configures the Azure Web App to deploy code directly from a GitHub repository using manual deployment integration.

`az webapp deployment source config`  
Links a source control repository to an Azure Web App for application deployment.
`--name Flask-App--CLI`: Specifies the target Azure Web App.
`--resource-group Static_WebCLI`: Identifies the resource group containing the web app.
`--repo-url`: GitHub repository URL containing the Flask application source code.
`--branch "main"`: Specifies the branch used for deployment.
`--manual-integration`: Disables automatic CI/CD triggers, requiring deployments to be manually initiated.
Verify Deployment:
`az>> webapp deployment source show --name Flask-App--CLI --resource-group Static_WebCLI`
<img width="1882" height="783" alt="Screenshot 2026-02-07 231451" src="https://github.com/user-attachments/assets/7870440f-5b27-4a9f-8fb9-c9e4f388c4a1" />

## Steps 6: Check Log Stream and Domain Name
**Command:**
`az>> webapp log tail --name Flask-App--CLI --resource-group Static_WebCLI
Streams live application logs from the Azure Web App to the terminal. This is used to debug deployment issues, startup failures, and runtime errors in real time.

`az webapp log tail`  
Connects to the web app’s log stream and outputs logs continuously.
`--name Flask-App--CLI`: Specifies the Azure Web App.
`--resource-group Static_WebCLI`: Identifies the resource group containing the web app.
<img width="1592" height="422" alt="Screenshot 2026-02-07 232144" src="https://github.com/user-attachments/assets/108f6e06-9217-4e64-b378-8df9671ae172" />

**Command:**
`az>> webapp show --name Flask-App--CLI --resource-group Static_WebCLI -o table
Retrieves the current configuration and runtime state of the Azure Web App and displays it in a readable table format.

`az webapp show`  
Fetches metadata and status information for an Azure Web App.
`--name Flask-App--CLI`: Name of the Azure Web App.
`--resource-group Static_WebCLI`: Resource group where the app is deployed.
`-o table`: Formats output as a table for readability.
<img width="1886" height="239" alt="Screenshot 2026-02-07 232832" src="https://github.com/user-attachments/assets/1c6e1ddc-596f-4c7e-88fb-d616061f1a57" />

<img width="575" height="271" alt="Screenshot 2026-02-07 232902" src="https://github.com/user-attachments/assets/dc26082b-aeed-42a3-8808-b9c8bb982ba3" />
