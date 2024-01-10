# Electric-Surf-Vegetables

## Overview
Electric-Surf-Vegetables is a Flask-based project designed for webhook handling with integrations to PostgreSQL for data persistence and RabbitMQ for message queuing. The project is optimized for minimal hardware resource usage and is containerized using Docker for ease of deployment.

## Getting Started

### Prerequisites
- Docker
- Python 3.8+
- Docker Compose

### Installation
Clone the repository and set up the project:

```
git clone https://github.com/IlanSpr/Electric-Surf-Vegetables/
cd Electric-Surf-Vegetables
docker-compose up --build
```

### Usage

#### Webhook Server
Access the webhook server at `http://localhost:5000/webhook`. It receives and processes POST requests, storing data in PostgreSQL and sending messages to RabbitMQ.

#### Vue.js Frontend
Access the frontend at `http://localhost:8080`. It displays a real-time business intelligence dashboard, updating with each webhook event.

#### Simulator Script
To test the webhook functionality:

```
python3 petzi_simulator.py http://localhost:5000/webhook mySecretKey
```

#### RabbitMQ Management Interface
Access the management interface at `http://localhost:15672` (default credentials: guest/guest). This interface allows you to monitor queues and messages.

### Development
For local development:

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Start the application:

   ```
   python3 petzi_webhook.py
   ```

### Testing
The `petzi_simulator.py` script is available for testing the webhook functionality.

### Database Verification
To access and verify data in the PostgreSQL database:

```
docker exec -it postgres_db bash
psql -U postgres
SELECT * FROM webhook;
```

### SSE Endpoint
Stream messages from RabbitMQ in real-time through Server-Sent Events (SSE) at the endpoint `http://localhost:5000/events`.

### Deployment
The project is fully containerized using Docker, making deployment straightforward and consistent across different environments.

### .env-example
Rename `.env-example` to `.env` and update it with your environment-specific settings.

## FOSS and Resource Efficiency
The project leverages Free and Open Source Software (FOSS) tools, optimized for limited hardware resources, including Flask, PostgreSQL, RabbitMQ, and Docker.
