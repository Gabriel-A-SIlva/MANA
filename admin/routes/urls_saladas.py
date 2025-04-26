from django.urls import path
from admin.views.management_saladas import create_saladas, read_saladas, update_saladas, delete_saladas

urlpatterns = [
    path('create_saladas/', create_saladas, name='create_saladas'),
    path('read_saladas/', read_saladas, name='read_saladas'),
    path('update_saladas/<int:salada_id>/', update_saladas, name='update_saladas'),
    path('delete_saladas/<int:salada_id>/', delete_saladas, name='delete_saladas'),
]