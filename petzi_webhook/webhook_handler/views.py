from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import hmac
import datetime
from .models import Buyer, Session, Ticket
import json

@csrf_exempt
@require_POST
def webhook(request):
    secret = b'secret'

    signature_with_timestamp = request.headers.get('Petzi-Signature')

    if not signature_with_timestamp:
        return HttpResponseForbidden("No signature provided")

    try:
        signature_parts = dict(part.split("=") for part in signature_with_timestamp.split(","))
        body = request.body.decode('utf-8')

        body_to_sign = f'{signature_parts["t"]}.{body}'.encode()

        expected_signature = hmac.new(secret, body_to_sign, "sha256").hexdigest()

        if not hmac.compare_digest(expected_signature, signature_parts["v1"]):
            return HttpResponseForbidden("Invalid signature")

        time_delta = datetime.datetime.utcnow() - datetime.datetime.fromtimestamp(int(signature_parts["t"]))
        if time_delta.total_seconds() > 30:
            return HttpResponseForbidden("Request timed out")

        data = json.loads(body)

        buyer_data = data.get('buyer', {})
        buyer, created = Buyer.objects.get_or_create(
            role=buyer_data.get('role', ''),
            first_name=buyer_data.get('firstName', ''),
            last_name=buyer_data.get('lastName', ''),
            postcode=buyer_data.get('postcode', '')
        )

        sessions = []
        for session_data in data.get('sessions', []):
            session, created = Session.objects.get_or_create(
                name=session_data.get('name', ''),
                date=session_data.get('date', ''),
                time=session_data.get('time', ''),
                doors=session_data.get('doors', ''),
                location_name=session_data.get('location_name', ''),
                street=session_data.get('street', ''),
                city=session_data.get('city', ''),
                postcode=session_data.get('postcode', '')
            )
            sessions.append(session)

        ticket_data = data.get('ticket', {})
        ticket = Ticket.objects.create(
            number=ticket_data.get('number', ''),
            type=ticket_data.get('type', ''),
            title=ticket_data.get('title', ''),
            category=ticket_data.get('category', ''),
            eventId=ticket_data.get('eventId', 0),
            event_name=ticket_data.get('event_name', 'default event name'),
            cancellationReason=ticket_data.get('cancellationReason', ''),
            promoter=ticket_data.get('promoter', 'default promoter'),
            price_amount=ticket_data.get('price_amount', 0.00),
            price_currency=ticket_data.get('price_currency', 'CHF'),
            buyer=buyer
        )

        for session in sessions:
            ticket.sessions.add(session)

        return JsonResponse({'status': 'success', 'message': 'Webhook processed successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

