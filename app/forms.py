from django import forms
from django.core import validators
def validate_for_a(data):
    if data.startswith("a"):
        raise forms.ValidationError("Validation for a")

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('Validation for length')

class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(5)])
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()
    email=forms.EmailField()
    confirmemail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError("Bot is Catched...")

    def clean(self):
        e=self.cleaned_data['email']
        ce=self.cleaned_data['confirmemail']
        if e!=ce:
            raise forms.ValidationError('emails are not matching....')

    