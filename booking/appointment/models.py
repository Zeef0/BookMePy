from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q, Min, F, Count, Manager, QuerySet
from django.urls import reverse
from django.utils import timezone


class AdminAppointmentManager(Manager):
    def get_queryset(self):
        return super().get_queryset(is_approved=False)

class AppointmentManager(Manager):
    def search_service(self, query=None):
        if query is None or query == "":
            return self.get_query().none()
        lookups = Q(service=query)
        return self.filter(lookups)

    def by_date(self, query=None):
        if query is None or query == "":
            return self.get_query().none()
        lookup = Q(appointment_time=query) | Q(date=query)
        return self.filter()

    def by_user(self, query=None):
        if query is None or query == "":
            return self.get_query().none()
        lookups = Q(username__username__contains=query) | Q(email__contains=query)
        return self.filter(lookups)


class Appointments(models.Model):
    AVAILABLE_HOURS = (
        ('8:00am', '8:00am'),
        ('9:30am', '9:30am'),
        ('11:00am', '11:00am'),
        ('1:00pm', '1:00pm'),
        ('2:30pm', '2:30pm'),
        ('4:00pm', '4:00pm'),
        ('6:00pm', '6:00pm')
    )

    AVAILABLE_SERVICES = (
        ("Doctor care", "Doctor care"),
        ("Nursing care", "Nursing care"),
        ("Medical social services", "Medical social services"),
        ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
    )

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, help_text="Enter your email Address", null=True)
    service = models.CharField(max_length=35, choices=AVAILABLE_SERVICES, default='Doctor Care')
    appointment_time = models.CharField(max_length=7, choices=AVAILABLE_HOURS, default='9:30am')
    date = models.DateField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    objects = AppointmentManager()
    admin = AdminAppointmentManager()

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ['-date', 'appointment_time']

    # def save(self, *args, **kwargs):
    #     super().save(args, kwargs)
    #     email = self.request.user.

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f'{self.username} | {self.email} | {self.service} | {self.appointment_time}'
