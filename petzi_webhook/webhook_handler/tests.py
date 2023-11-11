from django.test import TestCase

class PetziWebhookTestCase(TestCase):
    def test_petzi_webhook_handler(self):
        payload = '''
        {
            "event": "ticket_created",
            "details": {
                "ticket": {
                    "number": "XXXX2941J6SY",
                    "type": "online_presale",
                    "title": "My Parent Ticket",
                    "category": "My Category",
                    "eventId": 12345,
                    "event": "Event name",
                    "cancellationReason": "",
                    "sessions": [
                        {
                            "name": "Session name",
                            "date": "2023-04-28",
                            "time": "19:00:00",
                            "doors": "20:00:00",
                            "location": {
                                "name": "location",
                                "street": "2960 Curtis Course Suite 823",
                                "city": "East Monicaborough",
                                "postcode": "84458"
                            }
                        }
                    ],
                    "promoter": "Member name",
                    "price": {
                        "amount": "10.00",
                        "currency": "CHF"
                    }
                },
                "buyer": {
                    "role": "customer",
                    "firstName": "Jane",
                    "lastName": "Doe",
                    "postcode": "1234"
                }
            }
        }
        '''

        headers = {
            'Petzi-Signature': 't=1679476923,v1=7ed1d9929bcd41e2c2a206e0da91a00df7e6971e3bf33555a7',
            'Petzi-Version': '2'
        }

        response = self.client.post('/petzi_webhook/', data=payload, content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        print(response.content)
