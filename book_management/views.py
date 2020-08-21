from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    header_str = 'Hello, Python variable'
    template = loader.get_template('index.html')