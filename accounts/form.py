from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Provider


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField()
    city = forms.CharField()
    pincode= forms.CharField()
    address_text = forms.CharField()
    landmark = forms.CharField()
    google_map_Link = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.city=self.cleaned_data.get('city')
        customer.pincode=self.cleaned_data.get('pincode')
        customer.address_text=self.cleaned_data.get('address_text')
        customer.landmark=self.cleaned_data.get('landmark')
        customer.google_map_Link=self.cleaned_data.get('google_map_Link')
        
        customer.save()
        return user

    