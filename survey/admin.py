from django.contrib import admin

from survey.models import (
    CountryMaster, DistrictMaster, StateMaster, StateUniversitiesMaster)

# Register your models here.
admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(DistrictMaster)
admin.site.register(StateUniversitiesMaster)
