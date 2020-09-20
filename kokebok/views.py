from django.shortcuts import render
from .models import Course, Solution
from .serializers import CourseSerializer, SolutionSerializer
from rest_framework import generics
# Create your views here.


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SolutionListCreate(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

