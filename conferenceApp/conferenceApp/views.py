from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 


def index(request):
    return render(request, 'index.html')