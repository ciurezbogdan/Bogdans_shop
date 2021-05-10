from django.urls import path
from users.views.activation import activation_view, reset_token

app_name = 'activation'

urlpatterns = [
    path('activate/', activation_view, name='activate'),
    path('reset_token/', reset_token, name='reset_token'),
]
