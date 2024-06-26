# Generated by Django 4.0.6 on 2024-06-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0008_bugeffort_effor_status_alter_bug_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='bug_score',
            field=models.CharField(blank=True, choices=[('0', '--'), ('1', '15min'), ('2', '1hr'), ('3', '2hr'), ('4', '4hr'), ('5', '1day'), ('9', '16hr'), ('13', '24hr'), ('15', '32hr'), ('21', '1week')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bugeffort',
            name='percentage_completed',
            field=models.CharField(blank=True, choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], max_length=100, null=True),
        ),
    ]
