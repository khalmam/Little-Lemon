from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import MenuItem
from.serializers import MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu



# Create your views here.
def index(request):
  return render(request, 'index.html', {})
def sayHello(request):
 return HttpResponse('Hello World')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer



class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
     queryset = MenuItem.objects.all() 
     serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Booking.objects.all()
