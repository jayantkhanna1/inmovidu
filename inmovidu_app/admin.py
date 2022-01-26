from django.contrib import admin
from .models import company,job,student,apply
# Register your models here.
admin.site.register(company)
admin.site.register(job)
admin.site.register(student)
admin.site.register(apply)