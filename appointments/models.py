from django.db import models
from accounts.models import Status, Position, Title, Staff
from departments.models import Department

# Create your models here.


class Purpose(models.Model):
    """Model definition for Purpose."""

    name = models.CharField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Purpose."""

        verbose_name = 'Purpose'
        verbose_name_plural = 'Purposes'

    def __str__(self):
        """Unicode representation of Purpose."""
        return self.name


class Classification(models.Model):
    """Model definition for Classification."""
    name = models.CharField(max_length=350)

    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Classification."""

        verbose_name = 'Classification'
        verbose_name_plural = 'Classifications'

    def __str__(self):
        """Unicode representation of Classification."""
        return self.name


class Invite(models.Model):
    """Model definition for Invite."""
    visitor_name = models.CharField(max_length=350)
    phone_number = models.CharField(max_length=350)
    email = models.CharField(max_length=350)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    active_from = models.DateTimeField(auto_now=False)
    active_to = models.DateTimeField(auto_now=False)

    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    invited_by = models.CharField(max_length=350)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Invite."""

        verbose_name = 'Invite'
        verbose_name_plural = 'Invites'

    def __str__(self):
        """Unicode representation of Invite."""
        return self.visitor_name


class Appointment(models.Model):
    visitor_name = models.CharField(max_length=350)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now=False)
    host = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    """Model definition for Appointment."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Appointment."""

        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        """Unicode representation of Appointment."""
        return self.visitor_name


class VisitorRegistration(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=350)
    address = models.CharField(max_length=350)
    city = models.CharField(max_length=350)
    state = models.CharField(max_length=350)
    country = models.CharField(max_length=350)
    email = models.CharField(max_length=350)
    phone_contact = models.CharField(max_length=350)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="images/")
    signature = models.ImageField(upload_to="signature/")
    date = models.DateField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    """Model definition for VisitorRegistration."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for VisitorRegistration."""

        verbose_name = 'VisitorRegistration'
        verbose_name_plural = 'VisitorRegistrations'

    def __str__(self):
        """Unicode representation of VisitorRegistration."""
        return self.visitor_name
