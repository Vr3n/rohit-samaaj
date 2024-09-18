from django.db import models
from .validators import (validate_mobile_number_length,
                         string_only_contain_digits_validator,)
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CountryMaster(models.Model):
    country = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.country


class StateMaster(models.Model):
    state = models.CharField(max_length=256)
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.state


class DistrictMaster(models.Model):
    district = models.CharField(max_length=256)
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.district} from {self.state.state}"


class StateUniversitiesMaster(models.Model):
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE)
    university = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.university} from {self.state.state}"


class SamaajMember(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.father_name or ''} {self.mother_name or ''} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class SamaajMemberMobileNumber(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.PROTECT)
    mobile_number = models.CharField(
        max_length=10,
        validators=[
            string_only_contain_digits_validator,
            validate_mobile_number_length,
        ],
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"({self.samaaj_member.full_name}) - {self.mobile_number}"


# Model for Samaaj Member Email
class SamaajMemberEmail(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    email_address = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return f"({self.samaaj_member.full_name}) - {self.email_address}"


# Model for Samaaj Member Skills
class SamaajMemberSkills(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    year_of_experience = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"({self.samaaj_member.full_name}) skill set."


# Model for Samaaj Member Educational Qualification
class SamaajMemberEducationalQualification(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    QUALIFICATION_CHOICES = [
        ("SSC", "SSC"),
        ("HSC", "HSC"),
        ("Diploma", "Diploma"),
        ("PG", "PG"),
        ("OTHER", "Other"),
    ]
    qualification_name = models.CharField(max_length=10,
                                          choices=QUALIFICATION_CHOICES)
    name = models.CharField(max_length=100)
    qualification_year = models.IntegerField()

    def __str__(self) -> str:
        return f"({self.samaaj_member.full_name}) Educational Qualification."


# Model for Samaaj Member Address
class SamaajMemberAddress(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    flat_no_building_name = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200, blank=True, null=True)
    area = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    def __str__(self) -> str:
        return f"({self.samaaj_member.full_name}) Address."


# Model for Samaaj Member Mosaad
class SamaajMemberMosaad(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    taluka = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)


# Model for Samaaj Member Occupational Details
class SamaajMemberOccupationalDetails(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    OCCUPATION_CHOICES = [
        ("Business", "Business"),
        ("Service", "Service"),
        ("Farmer", "Farmer"),
        ("Labour", "Labour"),
        ("Other", "Other"),
    ]
    occupation_type = models.CharField(max_length=10,
                                       choices=OCCUPATION_CHOICES)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f"({self.samaaj_member.full_name}) Occupation Detail."
