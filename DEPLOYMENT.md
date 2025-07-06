# ALX Travel App - Deployment Guide

## Quick Start Guide

### 1. Environment Setup

```bash
# Clone the repository
git clone <your-repository-url>
cd alx_travel_app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Configuration

**MySQL Setup:**
```sql
-- Create database
CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (optional)
CREATE USER 'alx_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'alx_user'@'localhost';
FLUSH PRIVILEGES;
```

**Environment Variables:**
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your database credentials
# DB_NAME=alx_travel_db
# DB_USER=alx_user
# DB_PASSWORD=your_password
# SECRET_KEY=generate-a-new-secret-key
```

### 3. Django Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Create sample data (optional)
python manage.py create_sample_data

# Collect static files (for production)
python manage.py collectstatic
```

### 4. Running the Application

**Development:**
```bash
# Start Django development server
python manage.py runserver

# In another terminal, start Celery worker (optional)
celery -A alx_travel_app worker --loglevel=info
```

**Production with Gunicorn:**
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn alx_travel_app.wsgi:application --bind 0.0.0.0:8000
```

### 5. Access Points

- **Main Application:** http://localhost:8000/
- **Admin Interface:** http://localhost:8000/admin/
- **API Documentation:** http://localhost:8000/swagger/
- **Health Check:** http://localhost:8000/api/health/

## Project Structure Summary

```
alx_travel_app/
├── alx_travel_app/          # Main Django project
│   ├── settings.py          # ✅ Configured with MySQL, DRF, CORS, Swagger
│   ├── urls.py             # ✅ Swagger endpoints configured
│   ├── celery.py           # ✅ Celery configuration
│   └── __init__.py         # ✅ Celery app imported
├── listings/               # Django app
│   ├── models.py           # ✅ Listing model created
│   ├── views.py            # ✅ Health check API view
│   ├── urls.py             # ✅ API endpoints
│   ├── serializers.py      # ✅ DRF serializers
│   ├── admin.py            # ✅ Admin configuration
│   ├── tests.py            # ✅ Unit tests
│   └── management/         # ✅ Custom management commands
├── requirements.txt        # ✅ All dependencies listed
├── .env.example           # ✅ Environment template
├── .gitignore             # ✅ Git ignore rules
└── README.md              # ✅ Comprehensive documentation
```

## Features Implemented

✅ **Django Project Setup**
- Django 4.2.7 with modular structure
- Production-ready settings configuration

✅ **Database Configuration**
- MySQL database integration
- Environment-based configuration
- Migration support

✅ **API Framework**
- Django REST Framework setup
- CORS headers configuration
- Token authentication ready

✅ **API Documentation**
- Swagger/OpenAPI integration via drf-yasg
- Automatic documentation generation
- Interactive API explorer

✅ **Background Tasks**
- Celery configuration with Redis
- Task queue ready for scaling

✅ **Development Tools**
- Environment variable management
- Sample data creation command
- Comprehensive testing setup

✅ **Version Control**
- Git repository initialized
- Proper .gitignore configuration
- Commit history established

## Next Steps

1. **Customize Models:** Extend the Listing model with additional fields
2. **Add Authentication:** Implement user registration and JWT tokens
3. **API Endpoints:** Create full CRUD operations for listings
4. **Frontend Integration:** Connect with React/Vue.js frontend
5. **Deployment:** Configure for production with Docker/AWS

## Troubleshooting

**Common Issues:**

1. **MySQL Connection Error:**
   - Ensure MySQL server is running
   - Check database credentials in .env
   - Verify database exists

2. **Migration Issues:**
   ```bash
   python manage.py makemigrations listings
   python manage.py migrate
   ```

3. **Missing Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Swagger Not Loading:**
   - Check if drf-yasg is in INSTALLED_APPS
   - Verify URL configuration

For additional support, refer to the main README.md file.
