from django.shortcuts import render
from django.http import HttpResponse

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


