from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MessagesSerializer
from .models import Messages

# Create your views here.
class MessagesViewSet(viewsets.ModelViewSet):
  serializer_class = MessagesSerializer
  queryset = Messages.objects.all()