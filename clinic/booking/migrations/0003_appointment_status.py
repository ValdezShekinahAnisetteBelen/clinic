# Generated by Django 4.2.7 on 2023-11-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_appointment_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Processing', max_length=200),
        ),
    ]
