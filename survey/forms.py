from django import forms

from .models import (SamaajMember, SamaajMemberAddress,
                     SamaajMemberEducationalQualification,
                     SamaajMemberEmail,
                     SamaajMemberMobileNumber,
                     SamaajMemberOccupationalDetails)

from .validators import (
    validate_mobile_number_length,
    string_only_contain_digits_validator
)


class SamaajMemberForm(forms.ModelForm):
    mobile_number = forms.CharField(
        max_length=10,
        validators=[
            validate_mobile_number_length,
            string_only_contain_digits_validator
        ],
        required=False
    )

    class Meta:
        model = SamaajMember
        fields = "__all__"

    def save(self, commit=True):
        instance = super().save(commit=False)

        mobile_instance = SamaajMemberMobileNumber(
            mobile_number=self.cleaned_data['mobile_number']
        )
        mobile_instance.samaaj_member = instance
        mobile_instance.save()

        if commit:
            instance.save()
            self.save_m2m()

        return instance


class SamaajMemberEmailForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberEmail
        fields = "__all__"


class SamaajMemberMobileNumberForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberMobileNumber
        fields = "__all__"


class SamaajMemberAddressForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberAddress
        fields = "__all__"


class SamaajMemberEducationalQualificationForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberEducationalQualification
        fields = "__all__"


class SamaajMemberOccupationalDetailsForm(forms.ModelForm):
    class Meta:
        model = SamaajMemberOccupationalDetails
        fields = "__all__"


# Inline formsets for MobileNumber, Email, and Address
# SamaajMemberMobileNumberFormSet = inlineformset_factory(
#     SamaajMember,
#     SamaajMemberMobileNumber,
#     form=SamaajMemberMobileNumberForm,
#     extra=1,
# )
#
# SamaajMemberEmailFormSet = inlineformset_factory(
#     SamaajMember,
#     SamaajMemberEmail,
#     form=SamaajMemberEmailForm,
#     extra=1,
# )
#
# SamaajMemberAddressFormSet = inlineformset_factory(
#     SamaajMember,
#     SamaajMemberAddress,
#     form=SamaajMemberAddressForm,
#     extra=1,
# )
#
# SamaajMemberEducationalQualificationFormSet = inlineformset_factory(
#     SamaajMember,
#     SamaajMemberEducationalQualification,
#     form=SamaajMemberEducationalQualificationForm,
#     extra=1,
# )
#
# SamaajMemberOccupationalDetailsFormSet = inlineformset_factory(
#     SamaajMember,
#     SamaajMemberOccupationalDetails,
#     form=SamaajMemberOccupationalDetailsForm,
#     extra=1,
# )
