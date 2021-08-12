from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
	estudiantes = Student.objects.all()
	context = {'clase': 'Aprendiendo Django', 'estudiantes': estudiantes}
	return render(request, 'student_list.html', context)

def estudiantes(request, pk):
	return HttpResponse("Soy el estudiante numero: " + str(pk))