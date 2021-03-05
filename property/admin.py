from django.contrib import admin
import sys

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ["created_at"]

admin.site.register(Flat, FlatAdmin)

admin.site.site_header = "FLAT Admin"
admin.site.site_title = "FLAT Admin Portal"
admin.site.index_title = "Welcome to FLAT Portal"
