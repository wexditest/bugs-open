# Generated by Django 4.0.6 on 2024-06-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklystatusreport',
            name='efforts_status',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
