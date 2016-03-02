# django admin controll
from django.contrib import admin

from .models import Farm, Client, Crop, Ownership, Grows, Visit, Problem, Farm_has_visit, Visit_has_problem, Problem_type, Problem_specifics, Problem_has_specifics

# add the models/tables that you want to see at admin site
admin.site.register(Farm)
admin.site.register(Client)
admin.site.register(Crop)
admin.site.register(Ownership)
admin.site.register(Grows)
admin.site.register(Visit)
admin.site.register(Problem)
admin.site.register(Farm_has_visit)
admin.site.register(Visit_has_problem)
admin.site.register(Problem_type)
admin.site.register(Problem_specifics)
admin.site.register(Problem_has_specifics)


