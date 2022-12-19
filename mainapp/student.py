from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def student(request):
    if request.user.is_superuser == False and request.user.is_staff == False and request.user.is_active == True:
        return render(request , 'student/student.html')
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')