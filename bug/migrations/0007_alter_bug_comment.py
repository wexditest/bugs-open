# Generated by Django 4.0.6 on 2024-05-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0006_bugeffort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]