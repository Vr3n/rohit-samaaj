from django.contrib import admin

from survey.models import (
    CountryMaster, DistrictMaster, MobileNumberMaster,
    SamaajMember, SamaajMemberEmail,
    SamaajMemberMobileNumberMaster, StateMaster,
    StateUniversitiesMaster)

# Register your models here.
admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(DistrictMaster)
admin.site.register(StateUniversitiesMaster)
admin.site.register(SamaajMember)
admin.site.register(SamaajMemberMobileNumberMaster)
admin.site.register(MobileNumberMaster)
admin.site.register(SamaajMemberEmail)
