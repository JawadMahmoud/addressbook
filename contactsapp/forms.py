from django import forms
from contactsapp.models import Organization, Contact

class OrganizationForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name:")
    email = forms.CharField(max_length=128, required=False, help_text="Email:")
    address = forms.CharField(max_length=128, required=False, help_text="Address:")
    city = forms.CharField(max_length=128, required=False, help_text="City:")
    country = forms.CharField(max_length=128, required=False, help_text="Country:")
    logo = forms.ImageField(required=False, help_text="Company Logo:")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Organization
        fields = ('name', 'email', 'address', 'city', 'country', 'logo',)


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name:")
    address = forms.CharField(max_length=128, required=False, help_text="Address:")
    city = forms.CharField(max_length=64, required=False, help_text="City:")
    country = forms.CharField(max_length=64, required=False, help_text="Country:")
    phone = forms.CharField(max_length=16, required=False, help_text="Phone:")
    email = forms.CharField(max_length=128, required=False, help_text="Email:")
    role = forms.CharField(max_length=64, required=False, help_text="Position:")
    picture = forms.ImageField(required=False, help_text="Picture:")
    company = forms.ModelChoiceField(queryset=Organization.objects.order_by('name'), required=True, help_text="Company:")

    class Meta:
        model = Contact
        fields = ('name', 'address', 'city', 'country', 'phone', 'email', 'role', 'picture', 'company')