from django.urls import path
from admin.views.management_arrozes import create_arrozes, read_arrozes, update_arrozes, delete_arrozes

urlpatterns = [
    path('create_arrozes/', create_arrozes, name='create_arrozes'),
    path('read_arrozes/', read_arrozes, name='read_arrozes'),
    path('update_arrozes/<int:arroz_id>/', update_arrozes, name='update_arrozes'),
    path('delete_arrozes/<int:arroz_id>/', delete_arrozes, name='delete_arrozes'),
]