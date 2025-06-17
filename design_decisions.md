# 📐 Design Decisions: FastAPI Microservice

This document explains the key architectural and design decisions taken while building this FastAPI-based backend service using Celery, Redis, RabbitMQ, PostgreSQL, Docker, and SQLAlchemy.

---

## 1. ✅ FastAPI as the Web Framework

* Chosen for its speed (based on Starlette ASGI) and support for async endpoints.
* Built-in support for Pydantic ensures strong data validation.
* Auto-generates OpenAPI docs.

## 2. ✅ SQLAlchemy ORM with PostgreSQL

* PostgreSQL is a production-grade, ACID-compliant relational database.
* SQLAlchemy allows defining models and relationships cleanly.
* Configured with Alembic for database migrations.

## 3. ✅ Celery for Background Tasks

* Celery enables scheduling and executing long-running or async jobs outside request/response cycle.
* Example: Sending emails, processing data, etc.

## 4. ✅ Redis & RabbitMQ as Celery Brokers

* Redis is simple and fast (default broker).
* RabbitMQ supports advanced message queuing features (alternative broker).
* Flexibility to use either broker in `docker-compose.yml` and `.env`.

## 5. ✅ Docker + Docker Compose

* Full containerization using Docker.
* `docker-compose.yml` orchestrates FastAPI app, DB, Redis, RabbitMQ, and Celery worker.
* Ensures consistent local development and deployment.

## 6. ✅ Async-Ready Stack

* FastAPI routes are async for non-blocking I/O.
* Can integrate async SQLAlchemy in future if needed.

## 7. ✅ Alembic for DB Migrations

* Tracks and applies schema changes over time.
* Version-controlled migration history using `alembic/versions/`.

## 8. ✅ Modular Codebase

* Code organized into:

  * `api/` - route definitions
  * `schemas/` - request/response validation models
  * `crud/` - data access layer
  * `celery_tasks/` - background jobs
  * `db/` - DB setup and session management

## 9. ✅ Health Checks & Exception Handling

* `/health` endpoint for service monitoring.
* Custom exception handlers added to gracefully manage errors.

## 10. ✅ GitHub Versioning & Documentation

* README and this design doc provide setup, usage, and architecture details.
* Recommended: set up CI/CD and coverage reports in future.

---

## 📌 Tradeoffs & Future Improvements

* Currently uses sync SQLAlchemy; can migrate to async SQLModel.
* No authentication/authorization added yet.
* No unit tests — can be added using Pytest.
* No CI pipeline — can be integrated with GitHub Actions.

---

## 👨‍💻 Author: Ninaad Sanjay Bagul

Python Developer | Backend Engineer
GitHub: [https://github.com/ninaadbagul](https://github.com/ninaadbagul)
