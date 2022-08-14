import email
from django.contrib import admin
from college.models import College

# Register your models here.
class CollegeAdmin(admin.ModelAdmin):
    list_display=['name','email','address']
admin.site.register(College,CollegeAdmin) # exact class name  
