from django.http import HttpResponse

def index(request):
	return HttpResponse("TerpStats says hello world!")

def about(request):
	return HttpResponse("This is the about page")