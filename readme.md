# FastAPI Quickstart with Database Configuration

This repository provides a quickstart template for setting up a FastAPI application with a pre-configured PostgreSQL database.

## Getting Started

### Step 1: Create a `.env` File
Create a `.env` file in the root directory of the project and define the following environment variables:

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=fastapi
POSTGRES_HOST=localhost
POSTGRES_PORT=6000
```

### Step 2: Install Dependencies
Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Build and Start the Application
Use Docker Compose to build and start the application:

```bash
docker-compose up --build
```

### Step 4: Create a Database Migration
Generate a new database migration using Alembic:

```bash
alembic revision --autogenerate
```

### Step 5: Apply the Migration
Apply the migration to update the database schema:

```bash
alembic upgrade head
```

### Step 6: Start the Application
To start the application you need:

```bash
uvicorn app.main:app
```

## Notes
- Ensure Docker is installed and running on your system.
- The application will be accessible at `http://localhost:8000` by default.
- Update the `.env` file as needed for your specific environment.
