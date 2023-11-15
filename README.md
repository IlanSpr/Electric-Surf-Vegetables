# Electric-Surf-Vegetables

## Overview

This project, Electric-Surf-Vegetables, includes a Flask-based webhook (petzi_webhook.py) and a test simulator (petzi_simulator.py). The application is designed to handle incoming webhook requests and is containerized using Docker for easy and consistent deployment.

### Getting Started
#### Prerequisites

    Docker
    Python 3.8 or higher

#### Installation
Clone the repository and navigate to the project directory:


    git clone https://github.com/IlanSpr/Electric-Surf-Vegetables/
    cd Electric-Surf-Vegetables

Build and run the Docker container:

    docker-compose up --build

This command starts the Flask application inside a Docker container, exposed on port 5000.

### Usage
Webhook Server
The webhook server (petzi_webhook.py) is accessible at http://localhost:5000/webhook. It is configured to receive and process POST requests.

### Simulator Script
To test the webhook functionality, use the petzi_simulator.py script:

    python3 petzi_simulator.py http://localhost:5000/webhook

This script sends a simulated webhook request to the Flask server.

### Development
#### Running Locally
To run the Flask application locally (outside of Docker):
Install Python 3.8+ and the required dependencies:

    pip install -r requirements.txt

Start the application:

    python3 petzi_webhook.py

### Testing
Use petzi_simulator.py to test the webhook functionality. Ensure the Flask server is running before executing the simulator script.

### Deployment
The application is containerized using Docker, making it suitable for deployment on any system that supports Docker.
