from django.db import models
from django.contrib.auth.models import User
from datetime import date
import datetime
from datetime import datetime
import datetime

class WeeklyStatusReport(models.Model):
    us_bug_id = models.CharField(max_length=80,blank=True, null=True)
    us_bug_details = models.CharField(max_length=800,blank=True, null=True)
    assgined_to = models.ForeignKey(User,verbose_name = 'User Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    efforts = models.CharField(max_length=80,blank=True, null=True)
    efforts_status = models.CharField(max_length=80,blank=True, null=True)
    percentage_complete = models.CharField(max_length=100, blank=True, null=True)

    effort_date = models.DateField(default=datetime.date.today)



