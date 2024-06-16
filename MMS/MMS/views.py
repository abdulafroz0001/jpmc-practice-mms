
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from accounts import models
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')


#Department views --------------------------------------------------------------------------------------------------- 
def addDepartment(request):
    if request.method == 'POST':
        return render(request, 'department/addDepartment.html')
    return render(request, 'department/addDepartment.html')


#Course views --------------------------------------------------------------------------------------------------- 
def addCourse(request):
    if request.method == 'POST':
        return render(request, 'course/addCourse.html')
    return render(request, 'course/addCourse.html')


#Faculty views --------------------------------------------------------------------------------------------------- 
def addFaculty(request):
    if request.method == 'POST':
        return render(request, 'faculty/addFaculty.html')
    return render(request, 'faculty/addFaculty.html')



#Student views ---------------------------------------------------------------------------------------------------

def addStudent(request):
    if request.method == 'POST':
        stud_name = request.POST.get('stud_name')
        stud_age = request.POST.get('stud_age')
        stud_email = request.POST.get('stud_email')
        stud_phone = request.POST.get('stud_phone')
        stud_dept_id = request.POST.get('stud_dept')
        stud_deptment = models.Department.objects.filter(dept_id=stud_dept_id)[0]
        models.Student.objects.create(
                stud_name=stud_name,
                stud_age=int(stud_age),
                stud_email=stud_email,
                stud_phone=int(stud_phone),
                stud_dept=stud_deptment
            )
            
        return redirect('/students')  # Redirect to a page showing the list of students or a success page

    departments = models.Department.objects.all()
    
    return render(request, 'student/addStudent.html', context={'departments': departments})


def listStudents(request):
    students = models.Student.objects.all()
    print(students)
    return render(request, 'student/listStudents.html', context={'students': students})

def edit_student(request, stud_id):
    student = models.Student.objects.get(stud_id=stud_id)
    if request.method == 'POST':
        student.stud_name = request.POST['stud_name']
        student.stud_age = request.POST['stud_age']
        student.stud_email = request.POST['stud_email']
        student.stud_phone = request.POST['stud_phone']
        student.stud_dept = get_object_or_404(models.Department, dept_name=request.POST['stud_dept'])
        student.save()
        return redirect('list_students')
    return render(request, 'student/editStudent.html', {'student': student})

@require_http_methods(["GET", "POST"]) # type: ignore
def delete_student(request, stud_id):
    student = get_object_or_404(models.Student, stud_id=stud_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'student/deleteStudent.html', {'student': student})