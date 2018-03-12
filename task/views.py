from django.shortcuts import render
from log import log_info

# Create your views here.
def home(request):
    log_info.log_info()
    return render(request,'task/home.html')

def book(request):
    return render(request,'task/book.html')