from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#function based view
def home(request):
	html_var = 'vikram'
	
	return render(request, "base.html", {'html_var': html_var})

#class based view
