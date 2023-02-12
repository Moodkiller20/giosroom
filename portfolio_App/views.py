from django.shortcuts import render
from .models import *
# Create your views here.
def home_view(request):

    headline = "I am an honor student in Computer Science at Central Connecticut State University, with a proven track record of exceptional leadership, communication, technical writing, and coding abilities. My areas of interest include Software Engineering, Data Science, and Machine Learning. Throughout my academic and extracurricular pursuits, I have gained valuable experience as a supervisor, president, and manager in various projects, job responsibilities, and social activities."
    intro1 = "Greetings, I am Giovanni Tshibangu and I am passionate about creating software solutions. My journey in software development began in 2017, when I was first introduced to coding in my electronics class. This sparked my interest, leading me to make the decision to shift my focus from Electronic Engineering to Computer Science as my major."

    intro2="Today, I have been privileged to collaborate with local small businesses and have also had the opportunity to serve as a Software Engineer intern last summer. I have also been involved in various other projects. My current priority is to attain my Bachelor of Science degree, as I am currently a senior in college. I am equally invested in the areas of Artificial Intelligence and Data, with a aim to deepen my understanding of data mining and AI."

    recent_use_technologies=["Javascript (Jquery)","Android App dev. (Kotlin)","Python","Front-end framework (bootstrap)", "Back-end framework (Django)","Firebase","SQL"]

    """Get All relevant JOB experiences"""
    experiences = MyExperiences.objects.all()

    """Get All relevant Pojects"""
    projects = MyProjects.objects.all()

    """Get my Intro"""
    introduction = MyIntro.objects.all()
    print(introduction)




    context ={
        "intros":introduction,
        "recent_use_technologies":recent_use_technologies,
        "my_work_experiences":experiences,
        "projects": projects,



    }
    return render(request,"portfolio/home.html", context)