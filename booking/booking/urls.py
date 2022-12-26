from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('appointment.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('accounts/', include('allauth.urls'))

]
