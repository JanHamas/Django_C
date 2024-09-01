from django.shortcuts import render

def courseone(request):
    data = {
        'name':"hamas",
        'roll':49,
        'marks':500
    }
    return render(request,'courseone.html',{'data':data})
