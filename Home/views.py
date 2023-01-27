from django.shortcuts import render

# Create your views here.
def ind(request):
    return render(request,'test.html')
def index(request):
    return render(request,'index.html')