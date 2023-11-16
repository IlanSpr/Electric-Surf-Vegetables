# Electric-Surf-Vegetables

## Overview

This project, Electric-Surf-Vegetables, includes a Flask-based webhook (`petzi_webhook.py`) and a test simulator (`petzi_simulator.py`). The application handles incoming webhook requests and integrates with a PostgreSQL database, all containerized using Docker for easy and consistent deployment.

### Getting Started
#### Prerequisites

- Docker
- Python 3.8 or higher
- Docker Compose

#### Installation
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/IlanSpr/Electric-Surf-Vegetables/
cd Electric-Surf-Vegetables
```

Build and run the Docker containers:

```bash
docker-compose up --build
```

This command starts the Flask application and PostgreSQL database inside Docker containers. The Flask application is exposed on port 5000, and the database is accessible within the Docker network.

### Usage
#### Webhook Server
The webhook server (`petzi_webhook.py`) is accessible at `http://localhost:5000/webhook`. It is configured to receive POST requests and store data in the PostgreSQL database.

#### Simulator Script
To test the webhook functionality, use the `petzi_simulator.py` script:

```bash
python3 petzi_simulator.py http://localhost:5000/webhook
```

This script sends a simulated webhook request to the Flask server.

### Development
#### Running Locally
To run the Flask application locally (outside of Docker):
1. Install Python 3.8+ and the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the application:

    ```bash
    python3 petzi_webhook.py
    ```

### Testing
Use `petzi_simulator.py` to test the webhook functionality. Ensure the Flask server and PostgreSQL database are running before executing the simulator script.

### Database Verification
To verify the data stored in the PostgreSQL database:
1. Access the PostgreSQL container's command line:

    ```bash
    docker exec -it postgres_db bash
    ```

2. Connect to the PostgreSQL database:

    ```bash
    psql -U postgres
    ```

3. Run SQL queries to check the data:

    ```sql
    SELECT * FROM webhook;
    ```

### Deployment
The application is containerized using Docker, making it suitable for deployment on any system that supports Docker.

### .env-example
To configure the project with your environment-specific settings, rename .env-example to .env and update the file with your credentials and configuration details. This .env file will be used by Docker Compose to set environment variables for your Docker containers.
