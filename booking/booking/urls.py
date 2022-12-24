from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointment.urls')),
    path('user/', include('user.urls')),
    path('staff/', include('admin_rel.urls'))
]
