from django.contrib import admin

from survey.models import (
    CountryMaster, DistrictMaster,
    SamaajMember, SamaajMemberEmail,
    SamaajMemberMobileNumber,
    StateMaster,
    StateUniversitiesMaster)

# Register your models here.
admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(DistrictMaster)
admin.site.register(StateUniversitiesMaster)
admin.site.register(SamaajMember)
admin.site.register(SamaajMemberMobileNumber)
admin.site.register(SamaajMemberEmail)
