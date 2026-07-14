# Employee Asset Management System

A FastAPI-based backend application for managing employees and company assets. The system allows administrators to manage employees, assets, asset assignments, authentication using JWT, and provides dashboard analytics.

---

# Features

- Employee Management (CRUD)
- Asset Management (CRUD)
- Assign and Unassign Assets
- JWT Authentication
- Password Hashing using Bcrypt
- Dashboard Statistics
- PostgreSQL Database
- Alembic Database Migrations
- Docker Support
- Interactive Swagger Documentation

---

# Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT Authentication
- Passlib (Bcrypt)
- Docker
- Docker Compose

---

# Project Structure

```text
app/
│
├── core/
│   ├── auth.py
│
├── crud/
│
├── db/
│
├── models/
│
├── routers/
│
├── schemas/
│
├── main.py
│
alembic/
Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd emp-asset-mngmnt
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/employee_asset_management

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Migration

Generate migration

```bash
alembic revision --autogenerate -m "message"
```

Apply migrations

```bash
alembic upgrade head
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Application URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Docker Setup

Build and start the containers

```bash
docker compose up --build
```

Stop containers

```bash
docker compose down
```

---

# Authentication

The application uses JWT Bearer Authentication.

Workflow

1. Register a new user.
2. Login using email and password.
3. Receive an Access Token.
4. Click **Authorize** in Swagger.
5. Paste the token.
6. Access protected endpoints.

---

# API Endpoints

## Authentication

- POST /auth/register
- POST /auth/login

## Employees

- GET /employees
- GET /employees/{id}
- POST /employees
- PUT /employees/{id}
- DELETE /employees/{id}

## Assets

- GET /assets
- GET /assets/{id}
- POST /assets
- PUT /assets/{id}
- DELETE /assets/{id}

## Dashboard

- GET /dashboard

---

# Future Improvements

- Refresh Tokens
- Pagination
- Search and Filtering
- Role-Based Authorization
- Email Verification
- Audit Logs
- Unit Testing
- CI/CD Pipeline

---

# Author

**Mridul Sharma**