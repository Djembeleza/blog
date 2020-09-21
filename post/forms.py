from django.contrib.auth.models import User
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=50)
    emailAddress = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class UserForm(forms.ModelForm):
    email2 = forms.EmailField(label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'email2', 'password']

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Emails must match.')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already registered.")

        return email
