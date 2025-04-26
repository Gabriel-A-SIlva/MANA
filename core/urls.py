from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin.routes.urls_admin')),
    path('admin/proteinas/', include('admin.routes.urls_proteinas')),
    path('admin/arrozes/', include('admin.routes.urls_arrozes')),
    path('admin/saladas/', include('admin.routes.urls_saladas')),
]
