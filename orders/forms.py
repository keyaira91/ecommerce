from django import forms
from .models import Order



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city']
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        address = forms.CharField()
        postcode = forms.CharField()
        city = forms.CharField()
    