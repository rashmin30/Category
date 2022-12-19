from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


def upload_category(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        if 'submit' in request.POST:
            update_id = request.POST["update_id"]
            category = request.POST["category"]
            categorydiscrption = request.POST["categorydiscrption"]
            try:
                if update_id:
                    Category.objects.filter(categoryID = update_id).update(
                        categoryName = category,
                        categoryDiscription = categorydiscrption
                    )
                    messages.success(request , 'Category updated successfully')
                    return redirect('/superuser/view_category/')
                else:
                    obj = Category(
                        categoryName = category,
                        categoryDiscription = categorydiscrption
                    )
                    obj.save()
                    messages.success(request , 'Category store successfully')
                    return redirect('/superuser/view_category/')
            except Exception as ex:
                messages.error(request , f'{ex}')
                return redirect('/superuser/upload_category/')
        return render(request , 'category/upload_category.html')
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')    


def view_category(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        all_category_data = Category.objects.all().order_by('categoryID')
        delete_id = request.GET.get('delete_id')
        if delete_id:
            Category.objects.filter(categoryID = delete_id).delete()
            messages.success(request , 'Category deleted successfully.')
            return redirect('/superuser/view_category/')
        return render(request,'category/view_category.html' , { "all_category_data" : all_category_data })
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')


def update_category(request):
    update_id = request.GET.get('update_id')
    if update_id :
        update_category_data = Category.objects.get(categoryID = update_id)
    return render(request ,'category/upload_category.html', {"update_category_data" :update_category_data})