from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Menu, Booking

class UserSerializer (serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ['url', 'username','emails', 'groups']


        
class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id','title','price','inventory']        