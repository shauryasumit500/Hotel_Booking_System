from django import forms


class hotel_form(forms.Form):
    name=(forms.CharField())
    checkin_date =(forms.DateField())
    checkout_date = (forms.DateField())