from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


def all_houses(request):
    return HttpResponse(content="Hello")
