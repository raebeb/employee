from django.db import models
from applications.department.models import Department
class Employee(models.Model):
    """Model definition for employee"""

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )

    first_name = models.CharField("Primer nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    position = models.CharField("Cargo", max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.first_name} {self.last_name} -- {self.position}'