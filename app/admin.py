from django.contrib import admin

# Register your models here.
from .models import Module
from .models import Professor
from .models import ProfRating

admin.site.register(Module)
admin.site.register(Professor)
admin.site.register(ProfRating)