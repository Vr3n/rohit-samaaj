from django import forms
from .models import SamaajMember, SamaajMemberEmail, SamaajMemberMobileNumber


class SamaajMemberForm(forms.ModelForm):
    class Meta:
        model = SamaajMember
        fields = "__all__"


class SamaajMemberEmailForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberEmail
        fields = "__all__"


class SamaajMemberMobileNumberForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberMobileNumber
        fields = "__all__"
