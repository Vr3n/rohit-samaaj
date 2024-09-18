from typing import List, Union
from django.db.models import Q
from ninja import NinjaAPI
from django.core.exceptions import ValidationError as DjangoValidationError
from ninja.errors import HttpError, ValidationError
from survey.api.schema import (DistrictSchema, ErrorResponseSchema,
                               PersonalDetailFormSchema, StateBaseSchema,
                               SuccessResponseSchema)
from survey.models import (DistrictMaster, SamaajMemberEmail,
                           SamaajMemberMobileNumber,  StateMaster,
                           SamaajMember)

api = NinjaAPI()


@api.get("")
def hello(request):
    return {
        "message": "Hello, friend!",
    }


@api.get("/states", response=List[StateBaseSchema])
def states(request,
           state: Union[str, None] = None):
    if state is not None:
        try:
            queryset = StateMaster.objects.filter(
                state__icontains=state
            )
        except StateMaster.DoesNotExist:
            raise HttpError(404, "State Doesn't exist")
    else:
        queryset = StateMaster.objects.all()

    return queryset


@api.get("/districts/", response=List[DistrictSchema])
def districts(request,
              district: Union[str, None] = None,
              state: Union[str, None] = None):

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


@api.post("/personal-details/", response={201: SuccessResponseSchema,
                                          400: ErrorResponseSchema,
                                          422: ErrorResponseSchema, })
def personal_details(request, payload: PersonalDetailFormSchema):
    try:
        samaaj_member_obj = SamaajMember(
            first_name=payload.first_name,
            last_name=payload.last_name,
            mother_name=payload.mother_name,
            father_name=payload.father_name,
        )
        samaaj_member_obj.full_clean()
        samaaj_member_obj.save()

        mobile_no_obj = SamaajMemberMobileNumber(
            samaaj_member=samaaj_member_obj,
            mobile_number=payload.mobile_number,
        )
        mobile_no_obj.full_clean()
        mobile_no_obj.save()

        if payload.email_id is not None and payload.email_id != '':
            email_obj = SamaajMemberEmail.objects.create(
                samaaj_member=samaaj_member_obj,
                email_address=payload.email_id
            )
            email_obj.full_clean()
            email_obj.save()

    except ValidationError as e:
        raise HttpError(400, e)
    except DjangoValidationError as e:
        raise HttpError(400, e)
    return 201, {
        "message": "Member Personal Details Saved Succesfully!",
    }
