# Electric-Surf-Vegetables

## Overview
This Flask-based project handles webhook requests, integrates with a PostgreSQL database, and uses RabbitMQ for message queuing. It's designed for minimal hardware resource usage and is containerized using Docker.

## Getting Started
### Prerequisites
- Docker
- Python 3.8+
- Docker Compose

### Installation
Clone and set up the project:

    git clone https://github.com/IlanSpr/Electric-Surf-Vegetables/
    cd Electric-Surf-Vegetables
    docker-compose up --build

### Usage
#### Webhook Server
Access `http://localhost:5000/webhook`. Receives and processes POST requests.

#### Simulator Script
Test the webhook:

    python3 petzi_simulator.py http://localhost:5000/webhook mySecretKey


#### RabbitMQ Management Interface
Access at `http://localhost:15672` (default login: guest/guest).

### Development
Run locally:
1. Install dependencies: `pip install -r requirements.txt`
2. Start the application: `python3 petzi_webhook.py`

### Testing
Use `petzi_simulator.py` to test webhook functionality.

### Database Verification
Access and verify PostgreSQL data:
    
    docker exec -it postgres_db bash
    psql -U postgres
    SELECT * FROM webhook;

### Deployment
Containerized with Docker for easy deployment.

### .env-example
Rename to `.env` and update with your settings.

## FOSS and Resource Efficiency
Utilizes FOSS tools optimized for limited hardware resources: Flask, PostgreSQL, RabbitMQ, Docker.
