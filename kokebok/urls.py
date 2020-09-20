from django.urls import path
from . import views

urlpatterns = [
    path('api/course/', views.CourseListCreate.as_view() ),
    path('api/solution/', views.SolutionListCreate.as_view() ),
]
