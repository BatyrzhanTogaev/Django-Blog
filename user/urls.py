from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_page_view


urlpatterns = [
    path('login/', LoginView.as_view(), name='LoginPage'),
    path('logout/', LogoutView.as_view(next_page='/'), name='Logout'),
    path('register/', register_page_view, name='RegisterPage'),
]
