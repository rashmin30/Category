from django.urls import path
from .views import *
from .superuser import *
from .category import *




urlpatterns = [
    path('',index),
    path('check_user/',check_user),
    path('login/',user_login),
    path('logout/',user_logout),
    path('superuser/',superuser),
    path('superuser/upload_category/',upload_category),
    path('superuser/view_category/',view_category),
    path('superuser/view_category/update/',update_category),


]
