from django import forms

def validate_for_a(data):
    if data.startswith("a"):
        raise forms.ValidationError("Validation for a")

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('Validation for length')

class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_a,validate_for_len])
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()
    email=forms.EmailField()
    confirmemail=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirmPassword=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        e=self.cleaned_data['email']
        ce=self.cleaned_data['confirmemail']
        if e!=ce:
            raise forms.ValidationError('emails are not matching....')

    def clean(self):
        p=self.cleaned_data['password']
        cp=self.cleaned_data['confirmPassword']
        if p!=cp:
            raise forms.ValidationError("Password is not matching....")
