from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

User._meta.get_field('email')._unique = True


class MyIntro(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    head_text =  models.TextField(max_length=500, null=True, blank=True)
    intro_text =  models.TextField(max_length=500, null=True, blank=True)
    my_profile_picture = models.ImageField(upload_to="profile/", null=True, blank=True)

    about_me_intro1 =  models.TextField(max_length=500, null=True, blank=True)
    about_me_intro2 =  models.TextField(max_length=500, null=True, blank=True)

    tech_used1 =  models.CharField(max_length=70, null=True, blank=True)
    tech_used2=  models.CharField(max_length=70, null=True, blank=True)
    tech_used3 =  models.CharField(max_length=70, null=True, blank=True)
    tech_used4=  models.CharField(max_length=70, null=True, blank=True)
    tech_used5=  models.CharField(max_length=70, null=True, blank=True)
    tech_used6=  models.CharField(max_length=70, null=True, blank=True)

    my_email = models.CharField(max_length=70, null=True, blank=True)
    my_linkedIn = models.URLField(max_length=70, null=True, blank=True)
    my_instagram = models.URLField(max_length=70, null=True, blank=True)
    my_gitHub = models.URLField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.head_text


class MyExperiences(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    role =  models.CharField(max_length=140, null=True, blank=True)
    employer =  models.CharField(max_length=140, null=True, blank=True)
    employement_date =  models.CharField(max_length=140, null=True, blank=True)
    experience_descriptions1 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions2 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions3 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions4 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions5 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions6 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions7 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions8 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions9 = models.TextField(max_length=200, null=True, blank=True)
    experience_descriptions10 = models.TextField(max_length=200, null=True, blank=True)
    css_class =models.CharField(max_length=50, null=True, blank=True)
    css_id =models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.role + ' | ' + str(self.employer)

class MyProjects(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    proj_name =  models.CharField(max_length=140, null=True, blank=True)
    description =  models.TextField(max_length=400, null=True, blank=True)
    features1 = models.CharField(max_length=50, null=True, blank=True)
    features2 = models.CharField(max_length=50, null=True, blank=True)
    features3 = models.CharField(max_length=50, null=True, blank=True)
    features4 = models.CharField(max_length=50, null=True, blank=True)
    features5 = models.CharField(max_length=50, null=True, blank=True)

    tech_used = models.CharField(max_length=250, null=True, blank=True)

    proj_image_preview = models.ImageField(upload_to="projects/", null=True, blank=True)

    project_git_link = models.URLField()
    project_other_link = models.URLField()

    def __str__(self):
        return self.proj_name




