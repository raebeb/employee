from django.db import models
from applications.department.models import Department

class Hability(models.Model):
    """Model definition for Hability."""

    hability = models.CharField("Habilidad", max_length=50)

    class Meta:
        """Meta definition for Hability."""

        verbose_name = 'Hability'
        verbose_name_plural = 'Habilities'

    def __str__(self):
        return self.hability

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
    habilities = models.ManyToManyField(Hability)


    def __str__(self):
        return f'{self.first_name} {self.last_name} -- {self.position}'