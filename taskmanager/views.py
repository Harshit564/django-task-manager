# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone

def home(request):
    """
    Render index.html
    """
    now = timezone.now()
    return render(request, "taskmanager/index.html", {'now': now})

def home_files(request, file):
    """
    Render robots.txt or humans.txt
    """
    return render(request, file, content_type="text/plain")
