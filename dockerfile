# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    libpq-dev \
    python3-dev \
    build-essential \
    && apt-get clean

# Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Copy Nginx configuration file
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# Expose port 8000 for Django and 80 for Nginx
EXPOSE 8000 80

# Start Gunicorn and Nginx
CMD ["sh", "-c", "python manage.py migrate && gunicorn moyn.wsgi:application --bind 0.0.0.0:8000 & nginx -g 'daemon off;'"]
