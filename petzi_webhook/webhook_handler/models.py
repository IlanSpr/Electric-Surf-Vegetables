from django.db import models


class Ticket(models.Model):
    number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    eventId = models.IntegerField()
    event = models.CharField(max_length=100)
    buyer_first_name = models.CharField(max_length=50)
    buyer_last_name = models.CharField(max_length=50)
    buyer_postcode = models.CharField(max_length=10)

    def __str__(self):
        return self.title
