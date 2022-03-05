from django.contrib import admin
from tasks.models import NormalTasks, SpecialTasks, Completedtasks, SCompletedtasks

# Register your models here.
admin.site.register(NormalTasks)
admin.site.register(SpecialTasks)
admin.site.register(Completedtasks)
admin.site.register(SCompletedtasks)

