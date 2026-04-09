import os
import json
from django.conf import settings
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/ryanmontgomery.me/index.html')