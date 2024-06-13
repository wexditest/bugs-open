from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin



from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

# Register your models here.
class WeeklyStatusReportAdmin(ExportActionMixin, admin.ModelAdmin):
  list_display = ("us_bug_id","us_bug_details","assgined_to",'efforts','effort_date')
  list_filter = ("assgined_to","effort_date",("effort_date", DateRangeFilterBuilder()))

admin.site.register(WeeklyStatusReport, WeeklyStatusReportAdmin)
