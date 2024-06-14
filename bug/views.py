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


