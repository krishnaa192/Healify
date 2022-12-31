from django.forms import ModelForm
from .models import dept, booking_Appointments,package,have_query,subscription

from django import forms

#Bappointment bookng form
class BookingAppointmentsForm(ModelForm):
    class Meta:
        model = booking_Appointments
        fields=['Name', 'Email', 'Phone_no', 'department', 'description', 'slot','date']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class query_form(ModelForm):
    class Meta:
        model = have_query
        fields=['Name', 'Email', 'phone_no', 'related_dept', 'short_desc' ]


class subscriptionForm(ModelForm):
    class Meta:
        model=subscription
        fields=[ 'Email', 'Whatsapp_no']