from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessagesViewSet
from . import views


router = DefaultRouter()
router.register(r'messages', MessagesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    #path('api/get_data', MessagesViewSet.as_view({'get': "get_data"})),
    #path('api/post_data', MessagesViewSet.as_view({'post': "post_data"}))
    #path('api/Message_list/', views.message_list),
    
]