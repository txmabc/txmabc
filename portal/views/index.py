from django.shortcuts import render
from django.db import connection
import json


def index(request):
    return render(request, "portal/index.html", {"request": request})
