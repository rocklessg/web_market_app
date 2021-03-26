from django.http import HttpResponse
from django.shortcuts import render
from .models import Course


def index(request):
    iworld_market = Course.objects.all()
    return render(request, 'index.html', {'courses': iworld_market})
