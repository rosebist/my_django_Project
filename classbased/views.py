from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from crud.models import ClassRoom
from django.urls import reverse_lazy
from crud.forms import ClassRoomModelForm

# Create your views here.

class PortfolioView(TemplateView):
    template_name = 'myapp/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]= "Hello World"
        print(context)
        return context
    
    def get(self, request, *args, **kwargs):
        # Code to update Counter
        return super().get(request, *args, **kwargs)
    

class ClassRoomView(ListView):
    queryset = ClassRoom.objects.all()
    template_name = 'classbased/classroom.html'
    context_object_name = "classrooms"

class ClassRoomCreateView(CreateView):
    template_name = 'classbased/add_classroom.html'
    form_class = ClassRoomModelForm
    success_url = reverse_lazy('classbased_classroom')