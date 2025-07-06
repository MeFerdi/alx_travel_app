# ALX Travel App

A Django REST API application for a travel listing platform with comprehensive documentation and modern development practices.

## Features

- Django REST Framework API
- MySQL Database Configuration
- Swagger/OpenAPI Documentation
- CORS Support for Frontend Integration
- Celery for Background Tasks
- Environment Variable Management
- Production-Ready Configuration

## Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── celery.py           # Celery configuration
├── listings/               # Listings app
│   ├── models.py           # Database models
│   ├── views.py            # API views
│   ├── urls.py             # App URLs
│   ├── serializers.py      # DRF serializers
│   └── admin.py            # Django admin
├── requirements.txt        # Project dependencies
├── .env                   # Environment variables
└── manage.py              # Django management script
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL 5.7+ or 8.0+
- Redis (for Celery)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd alx_travel_app
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   
   Copy the `.env` file and update with your database credentials:
   ```bash
   DB_NAME=alx_travel_db
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   REDIS_URL=redis://localhost:6379/0
   ```

5. **Create MySQL database:**
   ```sql
   CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

6. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Documentation

The API documentation is automatically generated using Swagger and is available at:

- **Swagger UI:** http://localhost:8000/swagger/
- **ReDoc:** http://localhost:8000/redoc/
- **JSON Schema:** http://localhost:8000/swagger.json

## Available Endpoints

- `GET /api/health/` - Health check endpoint
- `GET /admin/` - Django admin interface
- `GET /swagger/` - Swagger API documentation
- `GET /redoc/` - ReDoc API documentation

## Development

### Running Celery

For background task processing:

```bash
# Start Celery worker
celery -A alx_travel_app worker --loglevel=info

# Start Celery beat (for scheduled tasks)
celery -A alx_travel_app beat --loglevel=info
```

### Database Management

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Testing

```bash
# Run tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## Technologies Used

- **Django 4.2.7** - Web framework
- **Django REST Framework 3.14.0** - API framework
- **drf-yasg 1.21.7** - Swagger documentation
- **django-cors-headers 4.3.1** - CORS support
- **django-environ 0.11.2** - Environment variable management
- **mysqlclient 2.2.0** - MySQL database adapter
- **Celery 5.3.4** - Background task processing
- **Redis 5.0.1** - Message broker and cache

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
