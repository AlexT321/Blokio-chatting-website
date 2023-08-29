from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessagesViewSet 
from . import views
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register(r'messages', MessagesViewSet)
app_name = 'core'

urlpatterns = [
    path("", include(router.urls)),
    path('api/get_data', MessagesViewSet.as_view({'get': "get_data"})),
    path('api/post_data', MessagesViewSet.as_view({'post': "post_data"})),
    path('register', views.register, name='register'),
    path('login', views.AccountTokenObtainPairView.as_view(), name='login'),
    path('user', views.detail, name='user'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    path('logout', jwt_views.TokenBlacklistView.as_view(), name='logout'),

]