from django.contrib import admin

# Register your models here.

from .models import Job, Job_ac

admin.site.register(Job)

admin.site.register(Job_ac)