from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', include('users.urls.account')),
    path('activation/<str:token>/', include('users.urls.activation')),
]
