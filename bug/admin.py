from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django import forms

from import_export.admin import ExportActionMixin



from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)




# Register your models here.

class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1

class StepsInline(admin.TabularInline):
    model = Steps
    extra = 1


class BugEffortInline(admin.TabularInline):
    model = BugEffort
    extra = 1

class CabModelForm(forms.ModelForm):
    comment = forms.CharField( widget=forms.Textarea )
    bug_title = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Bug
        fields = '__all__'



class BugAdmin(admin.ModelAdmin):
  form = CabModelForm
  list_display = ("kadet_id","bug_title","priority","dev_status","testing_status",'comment')
  inlines = [BugEffortInline,TestCaseInline, ]
  list_filter = ("release_det","assgined_to","board_obj",("start_date", DateRangeFilterBuilder()))

class TestCaseStepsAdmin(admin.ModelAdmin):
  list_display = ("test_case_name","comment")
  inlines = [StepsInline, ]



admin.site.register(Bug, BugAdmin)
admin.site.register(Board)
admin.site.register(ReleaseDetails)

admin.site.register(Steps)
admin.site.register(TestCaseSteps,TestCaseStepsAdmin)

