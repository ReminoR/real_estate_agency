from django.contrib import admin
import sys

from property.models import Flat, Complaint, Owner

class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', )

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', )
    readonly_fields = ("created_at",)
    list_display = ('id', 'address', 'price', 'new_building', )
    list_editable = ('new_building',)
    list_filter = ['new_building', 'floor', 'rooms_number']
    raw_id_fields = ('liked_by', )
    inlines = [OwnerInline,]

admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )

admin.site.register(Complaint, ComplaintAdmin)

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('owner', )
    raw_id_fields = ('flats', )

admin.site.register(Owner, OwnerAdmin)