from django.contrib import admin
from .models import *


class ClassesAdmin(admin.ModelAdmin):
    pass


class WeaponsCategoriesAdmin(admin.ModelAdmin):
    pass


class DicesAdmin(admin.ModelAdmin):
    pass


class CharsAdmin(admin.ModelAdmin):
    pass


class ArmorCategoryAdmin(admin.ModelAdmin):
    pass


class ToolsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Classes, ClassesAdmin)
admin.site.register(WeaponsCategories, WeaponsCategoriesAdmin)
admin.site.register(Dices, DicesAdmin)
admin.site.register(Chars, CharsAdmin)
admin.site.register(ArmorCategory, ArmorCategoryAdmin)
admin.site.register(Tools,ToolsAdmin)
