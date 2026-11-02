

\# Student Management System - DevOps Project



\## 1. Project Overview



The Student Management System is a simple Python application

used to manage student records.



It allows users to add, view, update and delete student details

and calculate average marks.



\## 2. Technologies Used



\- Python

\- Git

\- GitHub

\- Pytest

\- GitHub Actions

\- Docker



\## 3. Features



\- Add student details

\- View student details

\- Update student marks

\- Delete student records

\- Calculate average marks



\## 4. Automated Testing



Six automated test cases are implemented using Pytest.



\## 5. CI/CD Pipeline



GitHub Actions is configured to automatically execute

the test cases whenever code is pushed to the main branch

or a pull request targets the main branch.



\## 6. Docker



A Dockerfile is created to build the application image.

The application and automated tests are executed inside

a Docker container.



\## 7. How to Run the Application



Install dependencies:



python -m pip install -r requirements.txt



Run the application:



python student\_manager.py



Run automated tests:



python -m pytest -v



Build Docker image:



docker build -t student-management-app .



Run tests inside Docker:



docker run --rm student-management-app



Run the application inside Docker:



docker run -it --rm student-management-app python student\_manager.py



\## 8. Conclusion



This project demonstrates basic DevOps practices

by integrating Python application development,

version control, automated testing, CI/CD and

Docker containerization.



