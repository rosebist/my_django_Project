from django.shortcuts import render
from django.http import HttpResponse
from .models import ClassRoom

# Create your views here.
def home(request):
    return HttpResponse("""
<html>
<head>
<title>My project </title>
</head>
<body>
<h1> Hello world </h1>
</body>                                                                       
</html>                                               
                        

""")

def root_page(request):
    return render(request,template_name="myapp/root_page.html")

def temp_inherit(request):
    return render(request,template_name="myapp/temp_inherit.html")

def portfolio(request):
    return render(request,template_name="myapp/portfolio.html")
def classroom(request):
    classrooms = [
        {"name":"One","address": "KTM"},
        {"name":"Two","address": "PKR"},
        {"name":"Three","address": "Chabahil"},
        {"name":"four","address": "Chabahil"},
    ]
    return render(request,template_name="myapp/classroom.html",
                  context={"classroom_name":"one","location":"KTM", "classrooms":classrooms})


def classroomqs(request):
    classrooms= ClassRoom.objects.all()
    return render(request, template_name='myapp/classroom_qs.html', context={"classrooms":classrooms})