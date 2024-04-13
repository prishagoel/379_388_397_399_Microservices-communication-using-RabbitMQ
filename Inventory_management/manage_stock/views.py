from django.shortcuts import render
from django.http import HttpResponse

def bindex(request):
    return HttpResponse("INVENTORY MANAGEMENT SYSTEM: manage_stock app")