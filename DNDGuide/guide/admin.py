from django.contrib import admin
from .models import *


class ClassesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Classes, ClassesAdmin)
