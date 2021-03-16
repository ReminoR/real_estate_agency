from django.contrib import admin
import sys

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ("created_at",)
    list_display = ('price', 'new_building', 'construction_year',)
    list_editable = ('new_building',)
    list_filter = ['new_building', 'floor', 'rooms_number']

admin.site.register(Flat, FlatAdmin)
