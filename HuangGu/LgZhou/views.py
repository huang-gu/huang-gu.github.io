from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
def home(request):
    return render(request,'home.html')


