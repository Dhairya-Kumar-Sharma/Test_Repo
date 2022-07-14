import os
# import dotenv

# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from .password import random_password, temp_password
from .manager import CustomProfileManager

# Stores password
temp = temp_password()

# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(max_length = 100, blank = True, null = True, unique = False)
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default=random_password)
    auto_generated = models.BooleanField(default=False)
    objects = CustomProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def add_password(sender, instance, *args, **kwargs):
    
    if not instance.auto_generated:
        password = random_password()
        instance.set_password(password)
        temp.save_password(password)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_mail(sender, instance, created, **kwargs):
    password = temp.get_password
    print(f'\nLogin Credentials\nEmail: {instance.email}\nPassword: {password}') # Display Credentials to console
    if created:
        instance.auto_generated = True
        instance.save()
    #     dotenv.read_dotenv() # reading SENDGRID_API_KEY
    #     message = Mail(
    #         from_email='devender.singh@hestabit.in',
    #         to_emails=instance.email,
    #         subject=f'Welcome {instance.first_name}',
    #         html_content=f'Hello,<br>Your password is <strong>{password}</strong>.\
    #                         <br><br>This is a system generated email.')

    #     try:
    #         sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #         response = sg.send(message)
    #         print(response.status_code)
    #         print(response.body)
    #         print(response.headers)

    #     except Exception as e:
    #         print(e)
    #         print(e.body)
        
    # else:
    #     print('user not created')
