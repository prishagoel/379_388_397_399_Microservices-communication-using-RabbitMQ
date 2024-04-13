from django.shortcuts import render
from django.http import HttpResponse

def cindex(request):
    return HttpResponse("INVENTORY MANAGEMENT SYSTEM: schema app: I'VE CREATED SOME COOL TABLES!")
