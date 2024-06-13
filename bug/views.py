from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import openpyxl


def excel_index(request):
    if "GET" == request.method:
        return render(request, 'bug/excel_index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["DIR"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        count = 0
        for row in worksheet.iter_rows():
            row_data = list()

            for cell in row:
                if count > 0 :
                   row_data.append(str(cell.value))
            count = count + 1
            excel_data.append(row_data)

        return render(request, 'bug/excel_index.html', {"excel_data":excel_data})
"""
                Point

                Actual Hours

   x


                Expected Hours


                Sheet
    record_date = models.DateField(default=datetime.date.today)
    release_det = models.ForeignKey(ReleaseDetails,verbose_name = 'Release Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    bug_type = models.CharField(max_length=100, blank=True, null=True, choices=BUGSTATUS)
 f     bug_title =  cmodels.CharField(max_length=800,blank=True, null=True)
    assgined_to = fmodels.ForeignKey(User,verbose_name = 'User Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    dev_status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    testing_status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    priority = models.CharField(max_length=10, blank=True, null=True, choices=PRIORITY)
    end_date = models.DateField(default=datetime.date.today)
    bug_level = models.CharField(max_length=10, blank=True, null=True, choices=LEVELSTATUS)
    comment= models.CharField(max_length=100 ,blank=True, null=True)

                Reported Date

                Start Date

                End Date

                Board
                    board_obj =
                Board ID

                    board_id

                Kadet ID
                     kadet_id = m

                Type

                Details

                Assigned to

                Dev Status

                Assigned to(Test)

                Testing Status

                Level

                Comments

                Test Case ID
                """

"""
class ReleaseDetails(models.Model):
    release_name = models.CharField(max_length=80,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.release_name)

class Board(models.Model):
    board_name = models.CharField(max_length=80,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.board_name)



class Bug(models.Model):
    record_date = models.DateField(default=datetime.date.today)
    release_det = models.ForeignKey(ReleaseDetails,verbose_name = 'Release Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    board_obj = models.ForeignKey(Board,verbose_name = 'Board Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    board_id = models.CharField(max_length=80,blank=True, null=True)
    kadet_id = models.CharField(max_length=80,blank=True, null=True)
    start_date = models.DateField(default=datetime.date.today)
    bug_type = models.CharField(max_length=100, blank=True, null=True, choices=BUGSTATUS)
    bug_title =  cmodels.CharField(max_length=800,blank=True, null=True)
    assgined_to = fmodels.ForeignKey(User,verbose_name = 'User Name',default='', blank=True, null=True, on_delete=models.CASCADE)
    dev_status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    testing_status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    priority = models.CharField(max_length=10, blank=True, null=True, choices=PRIORITY)
    end_date = models.DateField(default=datetime.date.today)
    bug_level = models.CharField(max_length=10, blank=True, null=True, choices=LEVELSTATUS)
    comment= models.CharField(max_length=100 ,blank=True, null=True)


class TestCaseSteps(models.Model):
    test_case_name = models.CharField(max_length=80,blank=True, null=True)

    comment= models.CharField(max_length=100 ,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.test_case_name)


class Steps(models.Model):
    test_case_step_obj = models.ForeignKey(TestCaseSteps,verbose_name = 'TestCaseSteps',default='', blank=True, null=True, on_delete=models.CASCADE)
    step_count = models.CharField(max_length=80,blank=True, null=True)
    description = models.CharField(max_length=800,blank=True, null=True)
    action = models.CharField(max_length=800,blank=True, null=True)
    expected_result = models.CharField(max_length=800,blank=True, null=True)
    actual_result = models.CharField(max_length=800,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.step_count)


class TestCase(models.Model):
    bug_obj = models.ForeignKey(Bug,verbose_name = 'Bug Name',default='', blank=True, null=True, on_delete=models.CASCADE)

    rel_det_obj = models.ForeignKey(ReleaseDetails,verbose_name = 'Release',default='', blank=True, null=True, on_delete=models.CASCADE)
    test_case_obj = models.ForeignKey(TestCaseSteps,verbose_name='TestCase ID',default='', blank=True, null=True, on_delete=models.CASCADE)

    test_result = models.CharField(max_length=80,blank=True, null=True,choices=RESULT)

    comment= models.CharField(max_length=100 ,blank=True, null=True)








"""

