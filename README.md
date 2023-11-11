#Petzi Webhook Handler
##Overview

This Django application handles ticket_created webhook events from PETZI, storing ticket and buyer data in a database. It's currently in a testing phase and not suitable for production use.
Installation

Clone the repository and install dependencies:

    git clone [repository-url]
    pip install -r requirements.txt

Initialize the database:

    python manage.py migrate

Run the server:

    python manage.py runserver

Run tests with Django's test runner:

    python manage.py test

#Security Notice
The application bypasses signature verification in its current state. Implement proper request signature validation before using in production.
