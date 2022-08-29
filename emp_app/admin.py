from django.contrib import admin
from .models import Department,Role,Employee

# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','image','date']