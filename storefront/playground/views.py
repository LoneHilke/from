from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'Hello.html')







# fra https://www.youtube.com/watch?v=rHux0gMZ3Eg