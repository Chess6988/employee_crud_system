# Generated by Django 5.0.3 on 2024-09-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_employee_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
