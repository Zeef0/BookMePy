from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('appointments/', views.AppointmentsListView.as_view(), name='all_appointments'),
    path('user/panel', views.UserPanel.as_view(), name='user_panel'),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view(), name="appointment_detail"),
    path('book/appointment/', views.CreateAppointmentView.as_view(), name="book_appointment")
]
