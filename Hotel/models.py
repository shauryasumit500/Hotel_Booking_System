from django.db import models

# Create your models here.
class hotel_data(models.Model):
    customer_name = models.CharField(max_length=100)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    room_no = models.IntegerField()
