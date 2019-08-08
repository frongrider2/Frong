from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
	#return HttpResponse('<h1>Helloworld</h1>')
	return render(request,'mobile/home.html')

def About(request):
	return render(request,'mobile/about.html')

def Contact(request):
	return render(request,'mobile/contact.html')

def Ems(request):
	return render(request,'mobile/ems.html')