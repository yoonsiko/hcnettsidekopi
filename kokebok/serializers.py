from rest_framework import serializers
from .models import Course, Solution


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'subject', 'subject_code', 'nickname')


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'name', 'course', 'created_date', 'upload')

