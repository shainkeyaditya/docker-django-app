from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def createBlog(request):
	print('hello blog')
	return HttpResponse("First blog created")
