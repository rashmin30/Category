from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


def upload_sub_category(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        category_data = Category.objects.all().order_by("categoryID")
        if 'submit' in request.POST:
            update_id = request.POST["update_id"]
            subcategory = request.POST['subcategory']
            category = request.POST['category']
            for i in category_data:
                if i.categoryID == int(category):
                    main_category_data = i
            if update_id:
                SubCategory.objects.filter(subcategoryID = update_id).update(
                    subCategoryName = subcategory,
                    categoryID = main_category_data
                )
                messages.success(request , 'Subcategory are Updated successfully.')
                return redirect( '/superuser/view_sub_category/')
            else:
                obj = SubCategory(
                    subCategoryName = subcategory,
                    categoryID = main_category_data
                )
                obj.save()
                messages.success(request , 'Subcategory are saved successfully.')
                return redirect( '/superuser/view_sub_category/')
        return render(request , 'sub-category/upload_sub_category.html',{ "category_data" : category_data })
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')



def view_sub_category(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        all_sub_category_data = SubCategory.objects.all().order_by('subcategoryID')
        delete_id = request.GET.get('delete_id')
        if delete_id:
            SubCategory.objects.filter(subcategoryID = delete_id).delete()
            messages.success(request , 'Sub Category deleted successfully.')
            return redirect('/superuser/view_sub_category/')
        return render(request , 'sub-category/view_sub_category.html' , { "all_sub_category_data" : all_sub_category_data})
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')


def update_sub_category(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        category_data = Category.objects.all().order_by("categoryID")
        update_id = request.GET.get('update_id')
        if update_id:
            update_sub_category_data = SubCategory.objects.get(subcategoryID = update_id)
        return render(request , 'sub-category/upload_sub_category.html',{ "category_data" : category_data , "update_sub_category_data" :update_sub_category_data })
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')