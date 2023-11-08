import json
import hmac
import hashlib
from time import time
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket

SECRET_KEY = b'secret'


@csrf_exempt
def petzi_webhook_handler(request):
    if request.method == 'POST':
        try:
            # Step 1: Extract the timestamp and signature from the header
            provided_signature = request.headers.get('Petzi-Signature')
            version = request.headers.get('Petzi-Version')

            if not provided_signature or not version:
                return HttpResponseBadRequest("Missing signature or version")

            signature_parts = dict(part.split("=") for part in version.split(","))
            body_to_sign = f'{signature_parts["t"]}.{request.body.decode("utf-8")}'.encode()
            expected_signature = hmac.new(SECRET_KEY, body_to_sign, hashlib.sha256).hexdigest()

            # Step 4: Compare the signatures
            if not hmac.compare_digest(provided_signature, expected_signature):
                return HttpResponseBadRequest("Invalid signature")

            # Step 5: Check the timestamp
            time_delta = int(time()) - int(signature_parts["t"])
            if time_delta > 30:  # Allow requests within 30 seconds of timestamp
                return HttpResponseBadRequest("Invalid timestamp")

            # Extract and process the webhook data
            payload = json.loads(request.body)
            event_type = payload['event']

            # Extract relevant ticket information
            ticket_details = payload['details']['ticket']
            ticket_number = ticket_details['number']
            ticket_type = ticket_details['type']
            title = ticket_details['title']
            category = ticket_details['category']
            event_id = ticket_details['eventId']
            event_name = ticket_details['event']

            # Extract buyer information
            buyer_info = payload['details']['buyer']
            first_name = buyer_info['firstName']
            last_name = buyer_info['lastName']
            postcode = buyer_info['postcode']

            # Create or update the Ticket record
            ticket, created = Ticket.objects.update_or_create(
                number=ticket_number,
                defaults={
                    'type': ticket_type,
                    'title': title,
                    'category': category,
                    'eventId': event_id,
                    'event': event_name,
                    'buyer_first_name': first_name,
                    'buyer_last_name': last_name,
                    'buyer_postcode': postcode
                }
            )

            return HttpResponse("Webhook received successfully.")
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Invalid request method.")
