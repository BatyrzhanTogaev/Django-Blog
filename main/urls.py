from django.urls import path
from .views import home_page, created_post

urlpatterns = [
    path('', home_page, name='HomePage'),
    path('created', created_post, name='CreatedPage')
]
