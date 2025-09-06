from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'status', 'assigned_by', 'assigned_date')
    list_filter = ('status', 'assigned_by', 'assigned_date')
    search_fields = ('patient__name', 'doctor__name', 'assigned_by__email')
    readonly_fields = ('assigned_date', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Mapping Information', {
            'fields': ('patient', 'doctor', 'status', 'notes')
        }),
        ('System Information', {
            'fields': ('assigned_by', 'assigned_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
