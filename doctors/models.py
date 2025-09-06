from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('GP', 'General Practitioner'),
        ('CARD', 'Cardiologist'),
        ('NEURO', 'Neurologist'),
        ('ORTHO', 'Orthopedist'),
        ('DERMA', 'Dermatologist'),
        ('PEDIA', 'Pediatrician'),
        ('GYNEC', 'Gynecologist'),
        ('PSYCH', 'Psychiatrist'),
        ('ONCO', 'Oncologist'),
        ('EMERG', 'Emergency Medicine'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=10, choices=SPECIALIZATION_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    experience_years = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    available_hours = models.CharField(max_length=200, help_text='e.g., Mon-Fri 9AM-5PM')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Dr. {self.name} - {self.get_specialization_display()}'
