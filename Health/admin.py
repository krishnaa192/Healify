from django.contrib import admin
from . models import booking_Appointments,package,dept,have_query,subscription


# Register your models here.
admin.site.register(package)
admin.site.register(booking_Appointments)
admin.site.register(dept)
admin.site.register(have_query)
admin.site.register(subscription)