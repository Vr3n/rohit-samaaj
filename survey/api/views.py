from typing import List, Union
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from ninja import NinjaAPI
from ninja.errors import HttpError
from survey.api.schema import DistrictSchema
from survey.models import DistrictMaster, StateMaster

api = NinjaAPI()


@api.get("")
def hello(request):
    return {
        "message": "Hello, friend!",
    }


@api.get("/districts/", response=List[DistrictSchema])
def districts(request, district: Union[str, None] = None, state: Union[str, None] = None):

    if district is not None or state is not None:
        try:
            if district is None:
                queryset = DistrictMaster.objects.filter(
                    Q(state__state__icontains=state))
            elif state is None:
                queryset = DistrictMaster.objects.filter(
                    Q(district__icontains=district))
        except DistrictMaster.DoesNotExist:
            raise HttpError(404, "Query not found.")
    else:
        queryset = DistrictMaster.objects.all()

    return queryset
