from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.


def index(request):
	return render(request, 'reporting/index.html')
	

def result(request):
	cursor = connection.cursor()
	cursor.execute(request.POST['sql_data'])
	row = cursor.fetchall
	return row