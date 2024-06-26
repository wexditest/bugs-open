# Generated by Django 4.0.6 on 2024-05-20 15:20

import datetime
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
            name='WeeklyStatusReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('us_bug_id', models.CharField(blank=True, max_length=80, null=True)),
                ('us_bug_details', models.CharField(blank=True, max_length=800, null=True)),
                ('efforts', models.CharField(blank=True, max_length=80, null=True)),
                ('effort_date', models.DateField(default=datetime.date.today)),
                ('assgined_to', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Name')),
            ],
        ),
    ]
