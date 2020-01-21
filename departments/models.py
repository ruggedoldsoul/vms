from django.db import models

# Create your models here.



class Department(models.Model):
    dept_name=models.CharField(max_length=70)
    updated_at=models.DateTimeField(auto_now=True)
    deleted=models.BooleanField(default=False)

    
    """Model definition for Department."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return self.dept_name
