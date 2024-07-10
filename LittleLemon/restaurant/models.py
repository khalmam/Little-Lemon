from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bokingdate = models.DateField()

    
    
class Menu(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    inventory = models.IntegerField()

    