from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'placeholder': 'Your Name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'placeholder': 'Enter Your Email'}))
    phone = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'placeholder': 'Your Phone Number'}))
    address = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'placeholder': 'Your Address'}))
    date = forms.DateField(label='', widget=forms.DateInput(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'type': 'date', 'placeholder': 'Preferred Date'}))
    time = forms.TimeField(label='', widget=forms.TimeInput(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'type': 'time', 'placeholder': 'Preferred Time'}))
    service = forms.ChoiceField(label='', choices=[('babysitting', 'Babysitting'), ('educational', 'Educational Activities'), ('special', 'Special Care')], widget=forms.Select(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary'}))
    message = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={'class': 'form-control py-2 py-md-3 mb-3 mb-md-4 border-primary', 'rows': 6, 'cols': 10, 'placeholder': 'Additional Message'}))