from django.shortcuts import render
from notifyapp.views import index

def viewerpost(request):
    index(request)
    return render(request,'notifyapp/index.html')
