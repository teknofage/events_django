from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone

from .models import Event, Person, Group, Membership

from datetime import datetime

# Create your views here.

# function-based view
def greeting(request):
    html = "<html><body>Hello World!<body><html>"
    return HttpResponse(html)

# class-based view
class ShowBleating(View):
    def get(self, request):
        html = "<html><body>Hello World!</body></html>"
        return HttpResponse(html)