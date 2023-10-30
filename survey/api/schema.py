import re
from typing import Union
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
    email_id: str
    first_name: str
    last_name: str
    father_name: Union[str, None] = None
    mother_name: Union[str, None] = None

    @validator("mobile_number")
    def mobile_number_must_contain_ten_digits(cls, m: str) -> str:
        pattern = r'^\d{10}$'

        if re.match(pattern, m):
            raise ValueError("Enter Valid Mobile Number Format.")
        return m

    @validator("email_id")
    def email_id_format(cls, e: str) -> str:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.match(pattern, e):
            raise ValueError("Enter a valid email!")

        return e
