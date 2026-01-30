# **Python Flask App Deployment on Azure App Service**

This repository contains my **second hands-on Azure project**, created to get comfortable with the **Azure environment, governance, CI/CD, and deployment workflows** as preparation for a **cloud security career path**.

The application itself is intentionally simple. The real learning comes from deploying and operating it correctly in a real Azure environment.

---
<img width="681" height="285" alt="Screenshot 2026-01-29 214453" src="https://github.com/user-attachments/assets/f7152556-51d1-4a1f-84b0-5fd836261691" />

<img width="1616" height="498" alt="Screenshot 2026-01-29 220125" src="https://github.com/user-attachments/assets/8ffe76cc-0c64-4ed8-83b4-b38872c48f2a" />

<img width="1557" height="403" alt="Screenshot 2026-01-29 214212" src="https://github.com/user-attachments/assets/42d54cd4-2346-4da6-b30f-666877ceaa91" />

<img width="1362" height="577" alt="Screenshot 2026-01-29 215637" src="https://github.com/user-attachments/assets/1776546c-ff97-46f2-80ac-611f52703d7b" />


## **Project Overview**

- **Application:** Simple Python web application using Flask  
- **Cloud Platform:** Microsoft Azure  
- **Service:** Azure App Service (Linux)  
- **SKU / Plan:** Basic B1  
- **CI/CD:** GitHub Actions  
- **Runtime:** Python 3.10  

---

## **What I Built**

- A **basic Flask web application**
- Deployed it to **Azure App Service**
- Configured **environment variables** and **startup commands**
- Implemented **CI/CD using GitHub Actions**
- Used **Gunicorn** as the production server

---

## **Key Learnings**

- **Azure policy enforcement** (Student subscriptions allow deployments only in specific regions)
- Clear separation between **build time and runtime**
- How **Azure Oryx** handles dependency installation
- Writing and fixing **GitHub Actions workflows**
- Debugging deployments using **Azure Log Stream**
- Importance of **startup commands** and **health checks**
- Understanding **App Service SKUs** and resource usage (B1 plan)

---

## **Final Result**

The application successfully deploys and displays runtime configuration values such as:

- **Environment (ENV)**
- **Application version**

---

## **Why This Project Matters**

This project focuses on understanding how Azure behaves under real operational and governance constraints, which is foundational knowledge for a **cloud security-focused career**.
