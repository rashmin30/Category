from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

def superuser(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        return render(request , 'superuser/superuser.html')
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')


def userdata(request):
    if request.user.is_superuser == True:
        userdata = User.objects.all().order_by('id')
        blockid = request.GET.get('block')
        if blockid:
            User.objects.filter(id = blockid).update(
                is_active = False
            )
            messages.success(request , 'User Was Blocked.')
        unblockid = request.GET.get('unblock')
        if unblockid:
            User.objects.filter(id = unblockid).update(
                is_active = True
            )
            messages.success(request , 'User Was Unblocked.')
        return render(request , 'superuser/all-user.html' , {"userdata" : userdata})
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')