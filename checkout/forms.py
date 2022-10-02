from django import forms
from .models import Order


# Modified from Boutique Ado sample project.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone',
                  'street_address_1', 'street_address_2',
                  'town_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_city': 'Town or City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
        }

        # Makes the cursor begin in the full_name field.
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Add * to a required field.
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Setting placeholder attibutes.
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove form fields labels as placeholders do that job.
            self.fields[field].label = False