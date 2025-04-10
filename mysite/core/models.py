from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=50)
    position = models.TextField(max_length=100)
    date_applied = models.DateField()
    
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.position} at {self.company}"