from django.db import models

class Buyer(models.Model):
    role = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)  # Aligned with 'firstName' in JSON
    last_name = models.CharField(max_length=50)  # Aligned with 'lastName' in JSON
    email = models.EmailField(max_length=254, blank=True, null=True)  # New field for email
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Session(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    doors = models.TimeField()
    location_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=100, default='default event name')
    cancellation_reason = models.CharField(max_length=100, blank=True, null=True)
    promoter = models.CharField(max_length=100, default='default promoter')
    price_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_currency = models.CharField(max_length=10, default='CHF')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True, default=None)
    sessions = models.ManyToManyField(Session)

    def __str__(self):
        return self.title
