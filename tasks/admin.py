from django.contrib import admin
from .models import NormalTasks, SpecialTasks

# Register your models here.
admin.site.register(NormalTasks)
admin.site.register(SpecialTasks)
