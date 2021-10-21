from django.urls import path
from myapp.views import hello

urlpatterns = [
    path('', hello, name='hello'),
    path('<str:name>', hello, name='hello_name')
]
