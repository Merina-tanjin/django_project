from django.contrib import admin
from .models import Profile
from .models import Academic, Skill,User,Cv,Profile,Referee
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Cv)
admin.site.register(Academic)
admin.site.register(Referee)