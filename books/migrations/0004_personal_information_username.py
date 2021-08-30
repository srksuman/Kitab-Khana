# Generated by Django 3.2.6 on 2021-08-30 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_information',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]