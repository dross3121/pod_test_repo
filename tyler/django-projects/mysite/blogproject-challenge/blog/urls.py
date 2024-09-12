from django.urls import path
from . import views

urlpatterns = [
    # blog/
    path('', views.blog, name='blog'),
    # blog/edit/<int:post_id>
    path('edit/<int:post_id>', views.edit, name='edit'),
    # Create new post
    path('create/', views.create, name='create')
]