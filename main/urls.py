from django.urls import path
from .views import home_page, create_post, edit_post, delete_post, detail_post

urlpatterns = [
    path('', home_page, name='HomePage'),
    path('create/', create_post, name='CreatePage'),
    path('edit/<int:id>/', edit_post, name='EditPage'),
    path('delete/<int:id>/', delete_post, name='DeletePage'),
    path('detail/<int:id>/', detail_post, name='DetailPage')
]
