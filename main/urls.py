from django.urls import path
from .views import home_page, create_post, edit_post

urlpatterns = [
    path('', home_page, name='HomePage'),
    path('create/', create_post, name='CreatePage'),
    path('edit/<int:id>/', edit_post, name='EditPage'),
]
