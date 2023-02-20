from django.shortcuts import render
from .models import *
# Create your views here.
def home_view(request):


    """Get All relevant JOB experiences"""
    experiences = MyExperiences.objects.all()

    """Get All relevant Pojects"""
    projects = MyProjects.objects.all()

    """Get my Intro"""
    introduction = MyIntro.objects.all()
    print(introduction)




    context ={
        "intros":introduction,
        "my_work_experiences":experiences,
        "projects": projects,



    }
    return render(request,"portfolio/home.html", context)