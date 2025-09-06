from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'license_number', 'phone_number', 'user', 'created_at')
    list_filter = ('specialization', 'user', 'created_at')
    search_fields = ('name', 'license_number', 'phone_number', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'phone_number', 'email', 'address')
        }),
        ('Professional Information', {
            'fields': ('specialization', 'license_number', 'experience_years', 'consultation_fee', 'available_hours')
        }),
        ('System Information', {
            'fields': ('user', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
