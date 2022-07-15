# Generated by Django 4.0.5 on 2022-07-13 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_clientrequest_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientrequest',
            options={'verbose_name': 'Request', 'verbose_name_plural': 'Requests'},
        ),
        migrations.CreateModel(
            name='ChangeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo', models.CharField(max_length=150, verbose_name='Repository')),
                ('error', models.TextField(default='')),
                ('client_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_request', to='accounts.clientrequest')),
            ],
            options={
                'verbose_name': 'Change Request',
                'verbose_name_plural': 'Change Requests',
            },
        ),
    ]
