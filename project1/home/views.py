from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    data = {
        "stu1":{"name":"hamas","roll":66},       
        "stu2":{"name":"Jan","roll":62},       
        "stu3":{"name":"amas","roll":76},       
        "stu4":{"name":"Hairs","roll":96},       
        "stu5":{"name":"sultan","roll":86},
       
    }
    students = {"stu": data}
        
    return render(request,'index.html',students)
