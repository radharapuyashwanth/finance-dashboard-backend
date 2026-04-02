# Finance Data Processing and Access Control Backend

A backend assignment solution built with Django and Django REST Framework.

## Features

- Custom user model with roles: Viewer, Analyst, Admin
- Token-based authentication
- Financial record CRUD APIs
- Role-based access control
- Dashboard summary APIs
- Filtering, search, ordering, pagination
- Soft delete for records
- Input validation and proper error responses

## Role Access Rules

- **Viewer**: Can view records and dashboard summaries
- **Analyst**: Can view records and dashboard summaries
- **Admin**: Can create, update, soft delete records and manage users

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Setup Instructions

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Authentication

Generate token:

```http
POST /api/token/
```

Body:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Use header:

```http
Authorization: Token your_token_here
```

## Main APIs

### User Management (Admin only)

- `GET /api/users/`
- `POST /api/users/`
- `PUT /api/users/{id}/`
- `DELETE /api/users/{id}/`

### Financial Records

- `GET /api/records/`
- `POST /api/records/`
- `GET /api/records/{id}/`
- `PUT /api/records/{id}/`
- `DELETE /api/records/{id}/` (soft delete)

### Filters

Examples:

- `/api/records/?type=income`
- `/api/records/?category=Food`
- `/api/records/?start_date=2026-01-01&end_date=2026-03-31`
- `/api/records/?search=salary`
- `/api/records/?ordering=-amount`

### Dashboard Summary

- `GET /api/dashboard/summary/`

Returns:

- Total income
- Total expense
- Net balance
- Category-wise totals
- Recent activity
- Monthly trends

## Sample Admin User Creation via API

```json
{
  "username": "admin1",
  "email": "admin@example.com",
  "password": "Admin123",
  "role": "admin",
  "is_active": true
}
```

## Assumptions

- Authentication is implemented with DRF token authentication for simplicity.
- SQLite is used to keep setup simple.
- Soft delete is used instead of hard delete for records.
- Viewers and analysts are both read-only in this implementation.

## Suggested Improvements

- JWT authentication
- Unit tests
- Docker support
- Swagger/OpenAPI docs
- PostgreSQL for production
- Per-user data ownership restrictions if needed

## Project Notes

This solution focuses on correctness, maintainability, and clean backend structure rather than production-scale complexity.
