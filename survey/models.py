from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Model for Samaaj Member Mobile Number
class SamaajMemberMobileNumber(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    mobile_number = models.CharField(
        max_length=10,
        unique=True
    )  # Assuming a reasonable max length for mobile numbers
    is_whatsapp = models.BooleanField(default=False)


# Model for Samaaj Member Email
class SamaajMemberEmail(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    email_address = models.EmailField(unique=True)


# Model for Samaaj Member Skills
class SamaajMemberSkills(BaseModel):
    samaaj_member = models.ForeignKey(SamaajMember, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    year_of_experience = models.PositiveIntegerField()


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
