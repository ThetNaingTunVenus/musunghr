# Generated by Django 5.0.2 on 2024-02-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_attendance',
            name='checkout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
