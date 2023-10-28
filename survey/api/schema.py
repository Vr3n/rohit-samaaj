from ninja import Field, Schema


class CountrySchema(Schema):
    country: str


class StateBaseSchema(Schema):
    state: str
    country: CountrySchema = None


class StateDistrictSchema(Schema):
    state: str


class DistrictSchema(Schema):
    district: str
    state: str = Field(None, alias="state.state")
