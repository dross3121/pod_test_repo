from django.urls import path
from myapp.views import hello
from myapp.views import goodbye

urlpatterns = [
    path('', hello,name='hello'),
    path('<str:name>', hello, name='hello_name'),
    path('', goodbye,name='goodbye'),
    path('<str:name>', goodbye, name='goodbye_name'),
]