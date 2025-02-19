# Moyn Backend

This is the backend for the Moyn project, built with Django and Docker. It includes a PostgreSQL database and Nginx for serving static files and proxying requests.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. **Clone the repository**:

    ```sh
    git clone <repository-url>
    cd moyn-backend
    ```

2. **Create and start the Docker containers**:

    ```sh
    docker-compose up -d
    ```

3. **Run database migrations**:

    ```sh
    docker-compose exec web python manage.py migrate
    ```

4. **Load initial data fixtures**:

    ```sh
    docker-compose exec web python manage.py loaddata fixtures/users.json
    docker-compose exec web python manage.py loaddata fixtures/communities.json
    docker-compose exec web python manage.py loaddata fixtures/posts.json
    ```

5. **Create a superuser**:

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

6. **Collect static files**:

    ```sh
    docker-compose exec web python manage.py collectstatic
    ```

7. **Run locally**:

    ```sh
    docker-compose up db -d && DJANGO_DATABASE='local' ./manage.py runserver
    ```


## Services

- **Web**: The Django application running with Gunicorn.
- **Nginx**: Serves static files and proxies requests to the Django application.
- **PostgreSQL**: The database for the Django application.
- **pgAdmin**: A web-based database management tool for PostgreSQL.

## Accessing the Services

- **Django Application**: http://localhost:8000
- **Nginx**: http://localhost
- **pgAdmin**: http://localhost:8077

## Environment Variables

- **PIPENV_VENV_IN_PROJECT**: Set to `1` to create the virtual environment inside the project directory.
- **PIPENV_IGNORE_VIRTUALENVS**: Set to `1` to ignore existing virtual environments.

## Configuration

### Nginx

The Nginx configuration file is located at [nginx.conf](http://_vscodecontentref_/0). It is copied to the container at [nginx.conf](http://_vscodecontentref_/1).

### PostgreSQL

The PostgreSQL service is configured with the following environment variables:

- `POSTGRES_DB`: The name of the database.
- `POSTGRES_USER`: The username for the database.
- `POSTGRES_PASSWORD`: The password for the database.

### pgAdmin

The pgAdmin service is configured with the following environment variables:

- `PGADMIN_DEFAULT_EMAIL`: The default email for pgAdmin.
- `PGADMIN_DEFAULT_PASSWORD`: The default password for pgAdmin.

## Stopping the Services

To stop the Docker containers, run:

```sh
docker-compose down