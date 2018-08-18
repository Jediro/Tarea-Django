from django.shortcuts import render
from django.shortcuts import render_to_response
from alumnos.models import Alumno
from rest_framework import generics
from alumnos.serializer import AlumnoSerializer

class AlumnoList(generics.ListCreateAPIView):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()

class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()

def main(request):
    alumnos = Alumno.objects.all()
    return render_to_response("main.html", {'alumnos':alumnos})
