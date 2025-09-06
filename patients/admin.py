from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone_number', 'user', 'created_at')
    list_filter = ('gender', 'user', 'created_at')
    search_fields = ('name', 'phone_number', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'age', 'gender', 'phone_number', 'address')
        }),
        ('Medical Information', {
            'fields': ('medical_history', 'emergency_contact', 'emergency_phone')
        }),
        ('System Information', {
            'fields': ('user', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
