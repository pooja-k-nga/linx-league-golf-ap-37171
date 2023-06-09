from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from utils.models import BaseModel
from utils import generate_file_name


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, null=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )
    profile_image = models.ImageField(
        upload_to=generate_file_name, null=True, blank=True
    )
    weblink = models.URLField(
        blank=True,
        null=True,
    )
    business_name = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    street_address_2 = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    citizenship = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    birthdate = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]
    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        default="MALE",
    )
    social_security_number = models.CharField(max_length=255, blank=True, null=True)
    MARITAL_CHOICES = [
        ("MARRIED", "Married"),
        ("WIDOWED", "Widowed"),
        ("SEPARATED", "Separated"),
        ("DIVORCED", "Divorced"),
        ("SINGLE", "Single"),
    ]
    marital_status = models.CharField(
        max_length=15,
        choices=MARITAL_CHOICES,
        blank=True,
        null=True,
        default="MARRIED",
    )

    is_individual = models.BooleanField(
        blank=True,
        null=True,
    )
    is_organisation = models.BooleanField(
        blank=True,
        null=True,
    )
    is_anyone = models.BooleanField(
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )
    certification = models.FileField(
        upload_to=generate_file_name,
        blank=True,
        null=True,
    )
    has_ghin = models.BooleanField(
        default=False,
        blank=True,
        null=True,
    )
    ghin = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    friends = models.ManyToManyField("User", blank=True, related_name="user_friends")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return f"{self.user}"
