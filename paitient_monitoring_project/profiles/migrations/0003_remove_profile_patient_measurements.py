# Generated by Django 4.0.2 on 2022-02-20 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_patient_ids_profile_clinician_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='patient_measurements',
        ),
    ]
