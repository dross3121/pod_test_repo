from django.urls import path
from hello.views import hello

urlpatterns = [
    path('', hello, name='hello'),
    path('<str:name>', hello, name='hello_name'),
]
