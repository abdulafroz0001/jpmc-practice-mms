from django.db import models

class Department(models.Model):
    dept_id =models.AutoField(primary_key=True)
    dept_name= models.CharField(max_length=100)
    dept_email= models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.dept_name


class Course(models.Model):
    course_id= models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=100)
    course_credits= models.FloatField()
    course_dept= models.ForeignKey(Department, related_name="courseDept",on_delete=models.CASCADE)


class Student(models.Model):
    stud_id= models.AutoField(primary_key=True)
    stud_name=models.CharField(max_length=100)
    stud_age= models.IntegerField()
    stud_email= models.CharField(max_length=100)
    stud_phone = models.BigIntegerField()
    stud_dept= models.ForeignKey(Department, related_name="studentDept",on_delete=models.CASCADE)

class Faculty(models.Model):
    fac_id= models.AutoField(primary_key=True)
    fac_name=models.CharField(max_length=100)
    fac_age= models.IntegerField()
    fac_email= models.CharField(max_length=100)
    fac_phone = models.BigIntegerField()
    fac_dept= models.ForeignKey(Department, related_name="facultyDept",on_delete=models.CASCADE)



