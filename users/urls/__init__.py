from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.user_page import user_page_view, login_view
from users.views.user_profile import profile_view

app_name = 'users'

urlpatterns = [
    path('', include('users.urls.account')),
    path('activation/<str:token>/', include('users.urls.activation')),
    path('login_view/', login_view, name='login_view'),
    path('<int:user_id>/', user_page_view, name='user_page'),
    path('profile/', profile_view, name='profile')
]
