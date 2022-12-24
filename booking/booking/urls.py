from django.contrib import admin
from django.urls import path, include
from admin_rel.admin import admin_site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment_admin/', admin_site.urls),
    path('', include('appointment.urls')),
    path('user/', include('user.urls')),
    path('staff/', include('admin_rel.urls'))
]
