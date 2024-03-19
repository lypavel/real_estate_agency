from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('liked_by',)

    list_display = ('address', 'owner_pure_phone', 'price', 'new_building',
                    'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
