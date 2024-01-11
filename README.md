# Electric-Surf-Vegetables

## Introduction
Electric-Surf-Vegetables is an innovative Flask-based web application designed for real-time webhook handling and data visualization. It streamlines the process of tracking and analyzing webhook data such as ticket sales, making it ideal for live event management and similar applications.

## Overview
This application integrates PostgreSQL for robust data storage, RabbitMQ for efficient message queuing, and a Vue.js frontend to present a dynamic business intelligence dashboard. It's optimized for deployment in varied environments, courtesy of Docker containerization.

## Features
- **Real-Time Data Visualization**: The Vue.js frontend dynamically updates the business intelligence dashboard with each webhook event.
- **Scalable Architecture**: Using Flask, PostgreSQL, and RabbitMQ, the system is designed for high efficiency and scalability.
- **Docker Containerization**: Ensures seamless deployment and consistency across different environments.

## Architecture
![case-class-diagram](https://github.com/IlanSpr/Electric-Surf-Vegetables/assets/107176981/6929e00b-b310-4a03-8870-e1b69454af26)


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

```
python petzi_simulator.py http://localhost:5000/webhook mySecret
```


### Database Verification
To access and verify data in the PostgreSQL database:

```
docker exec -it postgres_db bash
psql -U postgres
SELECT * FROM webhook_event;
```

### SSE Endpoint
Stream messages from RabbitMQ in real-time through Server-Sent Events (SSE) at the endpoint `http://localhost:5000/events`.

### Deployment
The project is fully containerized using Docker, making deployment straightforward and consistent across different environments.

### .env-example
Rename `.env-example` to `.env` and update it with your environment-specific settings.

## FOSS and Resource Efficiency
The project leverages Free and Open Source Software (FOSS) tools, optimized for limited hardware resources, including Flask, PostgreSQL, RabbitMQ, and Docker.
