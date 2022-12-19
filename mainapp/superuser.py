from django.shortcuts import render,redirect
from django.contrib import messages


def superuser(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        return render(request , 'superuser/superuser.html')
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')