# AI API Test Platform

A backend REST API built with Python and FastAPI. This project demonstrates API development, database integration, data validation, and automated documentation using Swagger.

## Features

- FastAPI REST API
- SQLite database
- SQLAlchemy ORM
- Pydantic validation
- Create users with name and email
- Retrieve all users
- Interactive Swagger documentation
- Clean project structure
- GitHub-ready repository

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git

## Project Structure

```text
ai-api-test-platform/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── config.py
│   └── ai_helper.py
├── tests/
│   └── test_api.py
├── requirements.txt
├── README.md
└── .gitignore