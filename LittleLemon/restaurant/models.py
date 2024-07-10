from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    bokingdate = models.DateField()

    
    
class Menu(models.Model):
    id = models.IntegerField(max_length=6)
    title = models.CharField(max_length=255)
    price = models.DecimalField(10,2)
    inventory = models.IntegerField(max_length=5)

    