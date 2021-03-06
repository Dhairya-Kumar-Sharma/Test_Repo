# Generated by Django 4.0.5 on 2022-07-06 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cleint_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('code_link', models.TextField(verbose_name='Code')),
                ('token', models.CharField(max_length=200, verbose_name='Access Token')),
                ('version_control', models.CharField(max_length=50, verbose_name='Version Control')),
                ('branch', models.CharField(blank=True, max_length=50, null=True, verbose_name='Branch')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleint_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
