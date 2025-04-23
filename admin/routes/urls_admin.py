from django.urls import path
from admin.views.views_admin import index_admin, sign_in_admin, logout_view

urlpatterns = [
    path('', index_admin, name='index_admin'),
    path('sign_in_admin/', sign_in_admin, name="sign_in_admin"),
    path('logout_view/', logout_view, name="logout_view")
]
