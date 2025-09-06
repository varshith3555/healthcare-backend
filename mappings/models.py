from django.db import models
from django.contrib.auth import get_user_model
from patients.models import Patient
from doctors.models import Doctor

User = get_user_model()

class PatientDoctorMapping(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('COMPLETED', 'Completed'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_mappings')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    assigned_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['patient', 'doctor']
        ordering = ['-assigned_date']
    
    def __str__(self):
        return f'{self.patient.name} -> Dr. {self.doctor.name} ({self.status})'
