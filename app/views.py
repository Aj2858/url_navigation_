from django.shortcuts import render

# Create your views here.

def jspider(request):
    return render(request, 'ispider.html')