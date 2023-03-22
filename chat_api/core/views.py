from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MessagesSerializer
from .models import Messages
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
# Create your views here.

# @api_view(['Get'])
# def Messages_list(request):
#   messages = Messages.objects.all()
#   return Response(messages)
class MessagesViewSet(viewsets.ModelViewSet):
  serializer_class = MessagesSerializer
  queryset = Messages.objects.all()
  # print(queryset)

  @action(detail=False, methods=['get'])
  def get_data(self, request):
    data = Messages.objects.all()
    serializer = self.get_serializer(data, many=True)
    return Response(serializer.data)
  
  @action(detail=False, methods=['post'])
  def post_data(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


  
  # def index(self):
  #   return HttpResponse("Hello World")