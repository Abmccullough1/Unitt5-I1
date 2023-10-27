from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def hello_views(request: HttpRequest)-> HttpResponse:
    return HttpResponse("Hello World!")