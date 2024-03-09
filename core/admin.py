from django.contrib import admin
from .models import Academic, Skill,User,Cv,Profile,Referee


# Register your models here.
model_list = [ Skill,Cv,Academic,Profile,Referee]
admin.site.register(model_list)