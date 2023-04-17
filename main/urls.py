from django.urls import path
from .views import *

urlpatterns = [
    path('register',register,name='register'),
    path('get_or_update/<int:id>',update,name='get_or_update'),
    path('delete/<int:id>',delete,name='delete')
]
