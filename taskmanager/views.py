# -*- coding: utf-8 -*-
from django.shortcuts import render
 
def home(request):
    """
    Render index.html
    """
    return render(request, "taskmanager/index.html", {})
