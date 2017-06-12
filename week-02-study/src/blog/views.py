from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("나는  장고의 가장 기본이 되는 원리를 깨우쳐버렸다...")
