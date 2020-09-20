from django.db import models

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=25)
    subject_code = models.CharField(max_length=25)
    nickname = models.CharField(max_length=25)

    def __str__(self):
        return str(self.subject_code) + " " + str(self.subject)

class Solution(models.Model):
     name = models.CharField(max_length=25)
     course = models.ForeignKey(Course, on_delete=models.CASCADE)
     created_date = models.DateTimeField(auto_now_add = True)
     upload = models.FileField(upload_to='lf/')

     def __str__(self):
         return str(self.course.nickname) + " " + str(self.name)

