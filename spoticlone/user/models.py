from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500, blank=True)
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)

    def __str__(self):
        return str(self.user)

    def get_email(self):
        return str(self.email)

    def get_phone_number(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
