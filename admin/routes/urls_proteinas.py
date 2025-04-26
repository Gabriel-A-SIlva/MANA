from django.urls import path
from admin.views.management_proteinas import create_proteinas, read_proteinas, update_proteinas, delete_proteinas

urlpatterns = [
    path('create_proteinas/', create_proteinas, name='create_proteinas'),
    path('read_proteinas/', read_proteinas, name='read_proteinas'),
    path('update_proteinas/<int:proteina_id>/', update_proteinas, name='update_proteinas'),
    path('delete_proteinas/<int:proteina_id>/', delete_proteinas, name='delete_proteinas'),
]