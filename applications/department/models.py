from django.db import models


class Department(models.Model):
    """Model definition for Department."""

    name = models.CharField("Name", max_length=50)
    short_name = models.CharField("Short Name", max_length=50)
    is_active = models.BooleanField("Is Active", default=False)

    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return self.name


