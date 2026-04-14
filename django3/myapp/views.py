from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>Haqida Sahifasi</h1><p>Bu mening Django loyihasi haqida sahifasi.</p>')