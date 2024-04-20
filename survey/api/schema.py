import re
from typing import List, Union
from ninja import Field, Schema
from pydantic import validator


class CountrySchema(Schema):
    country: str


class StateBaseSchema(Schema):
    state: str
    country: str = Field(None, alias="country.country")


class StateDistrictSchema(Schema):
    state: str


class DistrictSchema(Schema):
    district: str
    state: str = Field(None, alias="state.state")


class SamaajMemberSchema(Schema):
    first_name: str
    last_name: str
    father_name: str
    mother_name: str


class PersonalDetailFormSchema(Schema):
    mobile_number: str
    email_id: Union[str, None] = None
    first_name: str
    last_name: str
    father_name: Union[str, None] = None
    mother_name: Union[str, None] = None

    @validator("mobile_number")
    def mobile_number_must_contain_digits_and_length_of_10(cls, m: str) -> str:
        pattern = r'^[0-9]*$'

        if not re.match(pattern, m) and len(m) != 10:
            raise ValueError(
                f"The Mobile number contains a alphabet or special character, and The length must be 10 digits, you have entered {len(m)} digits")
        elif len(m) != 10:
            raise ValueError(
                f"The Mobile number must be 10 digits, you have entered {len(m)} digits."
            )
        elif not re.match(pattern, m):
            raise ValueError(
                "The Mobile number contains a alphabet or special character It should contain only digits.")
        return m

    @validator("email_id")
    def email_id_format(cls, e: str) -> str:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not re.match(pattern, e):
            raise ValueError("Enter a valid email format!")

        return e


class SuccessResponseSchema(Schema):
    message: str


class ErrorDetail(Schema):
    field: str
    message: str


class ErrorResponseSchema(ErrorDetail):
    errors: List[ErrorDetail]

    @classmethod
    def from_validation_error(cls, validation_error):
        error_details = []
        for error in validation_error.errors():
            loc = ".".join(error['loc'])
            message = error["msg"]
            error_details.append(ErrorDetail(field=loc, message=message))
        return cls(errors=error_details)
