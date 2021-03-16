from django.contrib import admin
import sys

from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ("created_at",)
    list_display = ('price', 'new_building', 'construction_year',)
    list_editable = ('new_building',)
    list_filter = ['new_building', 'floor', 'rooms_number']
    raw_id_fields = ('liked_by', )

admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )

admin.site.register(Complaint, ComplaintAdmin)