from django import forms
from .models import UserProfile


# Modified from Boutique Ado sample project.
# Modified from checkout app forms.py.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_city': 'Town or City',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_county': 'State or County',
        }

        # Makes the cursor begin in the full_name field.
        self.fields['default_phone'].widget.attrs['autofocus'] = True

        # Field labels
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input')
            if field == "default_phone":
                self.fields[field].label = "Phone Number"
            if field == "default_street_address_1":
                self.fields[field].label = "Street Address, Line 1"
            if field == "default_street_address_2":
                self.fields[field].label = "Street Address, Line 2"
            if field == "default_town_city":
                self.fields[field].label = "Town or City"
            if field == "default_county":
                self.fields[field].label = "County or State"
            if field == "default_country":
                self.fields[field].label = "Country"
