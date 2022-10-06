from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 


def index(request):
    return render(request, 'index.html')


def organizing_commitee(request):
    return render(request, 'organizing_commitee.html')

def speakers(request):
    return render(request, 'speakers.html')


def venue(request):
    return render(request, 'venue.html')

def programme(request):
    return render(request, 'programme.html')

def awards(request):
    return render(request, 'awards.html')