from . models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


User = get_user_model()


class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This User is not active')

        log = super(UserLogin, self).clean(*args, **kwargs)
        return log


class CheckInForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request',None)
        super(CheckInForm,self).__init__(*args,**kwargs)

        CHOICES = (
            ('','Select Gender'),
            ('M', 'Male'),
            ('F', 'Female'),
        )

        self.fields['firstName'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'First Name','id':'firstName'}))

        self.fields['lastName'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'Last Name','id':'lastName'}))

        self.fields['gender'] = forms.ChoiceField(required=True,choices=CHOICES,
            widget=forms.Select(attrs={'class': 'form-detail', 'placeholder': 'Gender', 'id': 'gender'}))

        self.fields['dob'] = forms.DateField(required=True,
            widget=DateInput(attrs={'class': 'form-detail', 'placeholder': 'mm/dd/yyyy', 'id': 'dob'}))

        self.fields['address1'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'Street Address 1','id':'address1'}))

        self.fields['city'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'City','id':'city'}))

        self.fields['state'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'State','id':'state'}))

        self.fields['zipcode'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'form-detail', 'placeholder': 'Zip Code', 'id': 'zipcode'}))

        self.fields['phoneNumber'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'Phone Number','id':'phoneNumber'}))

        self.fields['driverLicense'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class':'form-detail','placeholder':'Driver License','id':'driverLicense'}))

        self.fields['checkin'] = forms.DateField(required=True,
            widget=DateInput(attrs={'class': 'form-detail', 'placeholder': 'mm/dd/yyyy', 'id': 'checkin'}))

        self.fields['checkout'] = forms.DateField(required=True,
            widget=DateInput(attrs={'class': 'form-detail', 'placeholder': 'mm/dd/yyyy', 'id': 'checkout'}))

        self.fields['adults'] = forms.IntegerField(
            widget=forms.TextInput(attrs={'class': 'form-detail', 'placeholder': 'No of Adults', 'id': 'adults'}))

        self.fields['children'] = forms.IntegerField(
            widget=forms.TextInput(attrs={'class': 'form-detail', 'placeholder': 'No of Children', 'id': 'children'}))

        self.fields['paymentAmount'] = forms.IntegerField(
            widget=forms.TextInput(attrs={'class': 'form-detail', 'placeholder': 'Payment Amount (Incl. Taxes)', 'id': 'paymentAmount'}))

        self.fields['petFee'] = forms.IntegerField(
            widget=forms.TextInput(attrs={'class': 'form-detail', 'placeholder': 'Pet Fee', 'id': 'petFee'}))

        self.fields['roomNumber'] = forms.IntegerField(
            widget=forms.TextInput(attrs={'class': 'form-detail', 'placeholder': 'Room Number', 'id': 'roomNumber'}))

    class Meta:
        guest = Guest
        widgets = {'dob': DateInput(), 'checkin': DateInput(), 'checkout': DateInput(),
                   }
        fields = [
            'driverLicense', 'firstName', 'lastName', 'gender',
            'address1', 'city', 'state', 'zipcode',
            'dob', 'phoneNumber',
            'checkin','checkout','adults', 'children',
            'paymentAmount','roomNumber','petFee',
        ]

    def save(self, commit=True):
        guest = Guest()
        guest.driverLicense = self.cleaned_data['driverLicense']
        guest.firstName = self.cleaned_data['firstName']
        guest.lastName = self.cleaned_data['lastName']
        guest.gender = self.cleaned_data['gender']
        guest.address1 = self.cleaned_data['address1']
        guest.city = self.cleaned_data['city']
        guest.state = self.cleaned_data['state']
        guest.zipcode = self.cleaned_data['zipcode']
        guest.dob = self.cleaned_data['dob']
        guest.phoneNumber = self.cleaned_data['phoneNumber']
        guest.checkin = self.cleaned_data['checkin']
        guest.checkout = self.cleaned_data['checkout']
        guest.adults = self.cleaned_data['adults']
        guest.children = self.cleaned_data['children']
        guest.paymentAmount = self.cleaned_data['paymentAmount']
        guest.petFee = self.cleaned_data['petFee']
        guest.roomNumber = self.cleaned_data['roomNumber']

        if commit is True:
            guest.save()

        return guest