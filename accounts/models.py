from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Title(models.Model):

    MR = 1

    MRS = 2

    MISS = 3

    TITLE_CHOICES = (
        (MR, 'mr'),
        (MRS, 'mrs'),
        (MISS, 'miss'),

    )

    id = models.PositiveSmallIntegerField(
        choices=TITLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Position(models.Model):
    name = models.CharField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    """Model definition for Position."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Position."""

        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        """Unicode representation of Position."""
        pass

    def __str__(self):
        return self.get_id_display()


class Status(models.Model):
    status_name = models.CharField(max_length=50)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    """Model definition for Status."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Status."""

        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        """Unicode representation of Status."""
        return self.status_name


class User(AbstractUser):
    picture = models.ImageField(upload_to="pictures/")
    title = models.ForeignKey(Title, null=True, on_delete=models.SET_NULL)
    is_visitor = models.BooleanField(default=False)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to="staff_uploads/", null=True)

    """Model definition for Staff."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Staff."""

        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        """Unicode representation of Staff."""
        return self.user.first_name
