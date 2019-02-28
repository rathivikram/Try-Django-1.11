from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#function based view
def home(request):
	guy = 'vikram'
	return HttpResponse(f"Hello {guy} to the world!")
	# return render(request, "home.html", {})