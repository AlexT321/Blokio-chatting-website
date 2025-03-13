from rest_framework import viewsets
from .serializers import MessagesSerializer
from .models import Messages
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers
from rest_framework import response
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt import views as jwt_views
from rest_framework import decorators as rest_decorators
from rest_framework import permissions as rest_permissions
from rest_framework import status as http_status
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
  
#new registration
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([])
def register(request):
    serializer = serializers.RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    
    user = serializer.save()
    return response.Response(status=http_status.HTTP_201_CREATED)
    

class AccountTokenObtainPairViewSerializer(jwt_serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class AccountTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = AccountTokenObtainPairViewSerializer


@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def detail(request):
    serializer = serializers.AccountSerializer(request.user)
    return response.Response({"user": serializer.data})
