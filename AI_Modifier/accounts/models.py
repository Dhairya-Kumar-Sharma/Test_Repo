from django.db import models
from modifier_admin.models import Profile

# Create your models here.
class ClientRequest(models.Model):
    url = models.URLField(verbose_name='URL', unique=True)
    code_link = models.TextField(verbose_name='Code')
    username = models.CharField(max_length=150, verbose_name='Username')
    token = models.CharField(max_length=200, verbose_name='Access Token')
    version_control = models.CharField(max_length=50, verbose_name='Version Control')
    branch = models.CharField(max_length=50, null=True, blank=True, verbose_name='Branch')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='client_request')