from django.shortcuts import render

# Create your views here.
def hello(request, name='world'):
    if request.method == 'GET':
        return render(request, 'hello.html', context = { 'name': name })
