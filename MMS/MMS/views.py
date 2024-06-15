
from django.shortcuts import render,redirect
from django.contrib import messages
from accounts import models 


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')


#Department views --------------------------------------------------------------------------------------------------- 
def addDepartment(request):
    if request.method == 'POST':
        data=request.POST
        dept_name=data.get('dept_name')
        dept_email=data.get('dept_email')
        

        dept=models.Department.objects.filter(dept_name=dept_name)
        if dept.exists():
            messages.error(request, "department already present")
            return redirect('/addDepartment') 

        models.Department.objects.create(dept_name=dept_name,dept_email=dept_email)
        messages.success(request, "deepartment added successfully")
        return redirect('/addDepartment') 
        
    return render(request, 'department/addDepartment.html')

def viewDepartment(request):
    departments=models.Department.objects.all()
    
    return render(request,"department/viewDepartment.html", context={'departments':departments})

def delDepartment(request,dept_id):
    dept=models.Department.objects.filter(dept_id=dept_id)
    dept.delete()
    return redirect('/viewDepartment')

def updateDepartment(request,dept_id):
    dept=models.Department.objects.filter(dept_id=dept_id)[0]
    if request.method=='POST':
        data=request.POST
        name=data.get('dept_name')
        email=data.get('dept_email')
         
        dept.dept_name=name
        dept.dept_email=email
        dept.save()
        return redirect('/viewDepartment')
    
    return render(request,"department/updateDepartment.html",context={'dept':dept})


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
