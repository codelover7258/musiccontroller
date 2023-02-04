from django.shortcuts import render
from rest_framework.generics import CreateAPIView # Post request (create room)
from .models import Room
from .serializers import RoomSerializer
# Create your views here.
class RoomView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer