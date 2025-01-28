# Event Management System

This document provides simple steps to run and access the Event Management System project.

---

## Overview

### 1. GitHub Repository

All source code, including the Dockerfile, requirements.txt, and documentation, is available in this repository:

[GitHub Repository](https://github.com/177smohammadzadeh/-EventManagementSystem)

### 2. Live Version (Google Cloud Run)

The project is deployed on Google Cloud Run. You can access it directly via this link:

https://eventmanagementsystem-916190127738.us-west1.run.app

#### Login Details
Use the following User Information to log in:
- **User:** admin
- **Password:** 123456

---

## How to Run the Project

### Option 1: Use the Live Version

You don’t need to install anything. Open the link below in your browser to access the project:

https://eventmanagementsystem-916190127738.us-west1.run.app

<img width="1707" alt="Screenshot 2025-01-28 at 01 00 20" src="https://github.com/user-attachments/assets/86627536-3b12-425f-b65b-f1a5d88aa7a5" />

---

### Option 2: Run Locally (Without Docker)

#### 1. Clone the Repository

git clone https://github.com/177smohammadzadeh/-EventManagementSystem

cd EventManagementSystem

#### 2. Set up Python Environment

Ensure Python 3.9 or later is installed on your system. Then create a virtual environment:

python -m venv venv

source venv/bin/activate  # On MacOS/Linux

venv\Scripts\activate  # On Windows

#### 3. Install Dependencies

Install required Python libraries:

pip install -r requirements.txt

#### 4. Run the Project

Start the Django development server:

python manage.py runserver

#### 5. Access the Project

Open your browser and go to:

http://127.0.0.1:8000

<img width="1710" alt="Screenshot 2025-01-28 at 01 15 34" src="https://github.com/user-attachments/assets/6615bcbd-bbc8-4934-8957-c45d5ea176c0" />

---

### Option 3: Run Locally with Docker

If you prefer to run the project on your local machine, follow these steps:

#### 1. Clone the Repository

Download the project from GitHub:

git clone https://github.com/177smohammadzadeh/-EventManagementSystem

cd EventManagementSystem

#### 2. Build the Docker Image

Create the Docker image:

in MacOs and Linux:

docker buildx build --platform linux/amd64 -t us-west1-docker.pkg.dev/eventmanagementsystem-449022/my-repo/eventmanagementsystem-main:latest --push .

For Windows(using Powershell):

docker buildx build --platform linux/amd64 -t your-docker-image-name:tag --push .

<img width="1710" alt="Screenshot 2025-01-28 at 01 26 34" src="https://github.com/user-attachments/assets/1e42b43f-3d6e-4de9-9c7b-1e4cd8e349de" />

#### 3. Run the Docker Container

Run the image locally:

docker run -p 8000:8000 event-management-system:latest

<img width="1710" alt="Screenshot 2025-01-28 at 01 28 01" src="https://github.com/user-attachments/assets/e7f7756f-9cd4-4637-80c9-14842f130026" />


#### 4. Access the Project

Open your browser and go to:

http://localhost:8000

### Project Structure
- `Dockerfile`: Contains the instructions to build the Docker image.
- `requirements.txt`: Contains all Python dependencies required to run the project.

Additional Notes
	•	All code and documentation are available in the GitHub repository.
	•	The live version on Google Cloud Run is provided for quick access.

If you have any questions, feel free to ask! 😊
