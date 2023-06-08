import time

import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    return render(request, 'home.html')


def index(request):
    return HttpResponse('Index page')


def health_check(request):
    time.sleep(5)
    return render(request, 'home.html')


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']  # Get the uploaded file from the request
        if file.name.endswith('.xlsx'):  # Check if the file is in Excel format
            df = pd.read_excel(file)  # Read the Excel file using pandas
            records = df.to_dict('records')  # Convert DataFrame to a list of dictionaries

            # Print each record
            for record in records:
                print(record)

            return HttpResponse('upload_success')
        else:
            return HttpResponse('upload_failure')

    return HttpResponse('check method of upload_file....')
