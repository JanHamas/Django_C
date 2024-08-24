from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    data = {
        "stu1":{"name":"hamas"}
    }
        
    return render(request,'index.html',student)
