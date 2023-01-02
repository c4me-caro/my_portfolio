from django.shortcuts import render
from .models import Project

# Create your views here.
def home(req):
    projects = Project.objects.all()
    return render(req, 'home.html', {'title': 'Inicio', 'projects' : projects})