
from django.shortcuts import render

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
        return render(request, 'student/addStudent.html')
    return render(request, 'student/addStudent.html')


#admin views ------------------------------------------------------------------------------------------------------

def adminDashboard(request):
    return render(request, 'admin/adminDashboard.html')