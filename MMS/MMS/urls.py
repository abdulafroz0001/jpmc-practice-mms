"""MMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('', views.index,name=''),
    path('dashboard',views.dashboard,name='dashboard'),
    #Department routes ---------------------------------------------------------------------------------------------------
    path('addDepartment',views.addDepartment,name='add-department'),
    path('viewDepartment',views.viewDepartment,name='view-department'),
    path('delDepartment/<dept_id>',views.delDepartment,name='delDepartment'),
    path('updateDepartment/<dept_id>',views.updateDepartment,name='updateDepartment'),
    #Course routes -------------------------------------------------------------------------------------------------------
    path('addCourse',views.addCourse,name='add-course'),


    #Faculty routes ------------------------------------------------------------------------------------------------------
    path('addFaculty',views.addFaculty,name='add-faculty'),


    #Student routes ------------------------------------------------------------------------------------------------------
    path('addStudent/',views.addStudent,name='add-student'),
    path('students/', views.listStudents, name='list_students'),
    path('edit_student/<int:stud_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:stud_id>/', views.delete_student, name='delete_student'),


    #Admin routes --------------------------------------------------------------------------------------------------------

    # path('adminDashboard',views.adminDashboard,name='admin-dashboard'),

]
