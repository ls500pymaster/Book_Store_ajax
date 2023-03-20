from django.contrib import admin

from app.models import Number, Car


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('username', 'number')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "engine_cc", "style")
