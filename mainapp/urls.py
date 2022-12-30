from django.urls import path
from .views import *
from .superuser import *
from .category import *
from .sub_category import *


urlpatterns = [
    path('', index),
    path('check_user/', check_user),
    path('login/', user_login),
    path('logout/', user_logout),
    path('superuser/', superuser),
    path('superuser/upload_category/', upload_category),
    path('superuser/view_category/', view_category),
    path('superuser/view_category/update/', update_category),
    path('superuser/upload_sub_category/', upload_sub_category),
    path('superuser/view_sub_category/', view_sub_category),
    path('superuser/view_sub_category/update/', update_sub_category),
    path('all-user', userdata),



]
