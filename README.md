# Student Management System - DevOps Project 🐍

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Testing-Pytest-orange?logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/Containerization-Docker-blue?logo=docker&logoColor=white)

This repository contains a **Student Management System** developed using Python and integrated with DevOps practices to automate testing and prepare the application for deployment.

**Purpose:** To understand and implement DevOps practices such as version control, automated testing, CI/CD pipelines, and Docker containerization.

---

## 📑 Table of Contents

- [Project Overview](#1-project-overview)
- [Technologies Used](#2-technologies-used)
- [Features](#3-features)
- [Project Structure](#4-project-structure)
- [Automated Testing](#5-automated-testing)
- [CI/CD Pipeline](#6-cicd-pipeline)
- [Docker Containerization](#7-docker-containerization)
- [How to Run the Application](#8-how-to-run-the-application)
- [Conclusion](#9-conclusion)
- [Author](#10-author)

---

## 1. Project Overview

The Student Management System is a simple Python application used to manage student records.

It allows users to add, view, update, and delete student details and calculate the average marks of students.

This project demonstrates how DevOps practices can be applied to a Python application to automate testing and prepare it for deployment.

## 2. Technologies Used

- **Python 3.14** – Application development
- **Git** – Version control
- **GitHub** – Source code repository
- **Pytest** – Automated testing
- **GitHub Actions** – CI/CD automation
- **Docker** – Application containerization
- **PowerShell** – Command-line operations

## 3. Features

- Add student details
- View student details
- Update student marks
- Delete student records
- Calculate average marks
- Validate student details and marks
- Display error messages for invalid operations

## 4. Project Structure

```text
Student-Management-Devops/
│
├── student_manager.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
│
├── tests/
│   └── test_student_manager.py
│
└── .github/
    └── workflows/
        └── python-tests.yml
```

## 5. Automated Testing

Automated testing is implemented using the **Pytest** framework.

Six test cases are created to verify the application functionality.

The test cases include:

1. Add a student
2. View student details
3. Update student marks
4. Delete a student
5. Calculate average marks
6. Validate invalid marks

**Command to run automated tests:**

```powershell
python -m pytest -v
```

Expected result: All six test cases should pass successfully.

## 6. CI/CD Pipeline

GitHub Actions is used to automate the testing process.

A workflow file named `python-tests.yml` is created inside the `.github/workflows` directory.

The pipeline performs the following steps:

1. Checks out the GitHub repository.
2. Sets up Python 3.14.
3. Installs project dependencies.
4. Executes automated test cases using Pytest.

The workflow runs automatically whenever code is pushed to the `main` branch or a pull request targets the `main` branch.

## 7. Docker Containerization

Docker is used to package the application and its dependencies into a Docker image.

A Dockerfile is created using the Python 3.14 slim base image.

**Docker commands:**

Build Docker image:

```powershell
docker build -t student-management-app .
```

View Docker images:

```powershell
docker images
```

Run automated tests inside the Docker container:

```powershell
docker run --rm student-management-app
```

Run the Student Management System inside Docker:

```powershell
docker run -it --rm student-management-app python student_manager.py
```

## 8. How to Run the Application

**Step 1: Clone the repository**

```powershell
git clone https://github.com/ShaikNasreenNov25/Student-Management-CI-CD-Pipeline.git
```

**Step 2: Open the project directory**

```powershell
cd Student-Management-CI-CD-Pipeline
```

**Step 3: Install dependencies**

```powershell
python -m pip install -r requirements.txt
```

**Step 4: Run the application**

```powershell
python student_manager.py
```

**Step 5: Run automated tests**

```powershell
python -m pytest -v
```


## 9. Conclusion

This project demonstrates the implementation of basic DevOps practices by integrating Python application development, Git version control, automated testing, GitHub Actions CI/CD, and Docker containerization.

It helps understand how software testing can be automated and how an application can be prepared for deployment using DevOps tools.

## 10. Author

- **Name:** Shaik Nasreen
- **GitHub:** [ShaikNasreenNov25](https://github.com/ShaikNasreenNov25)
- **Project Repository:** [Student Management CI/CD Pipeline](https://github.com/ShaikNasreenNov25/Student-Management-CI-CD-Pipeline)

---

**Thank you for visiting this project!**
