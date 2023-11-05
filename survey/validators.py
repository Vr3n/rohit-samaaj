from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_mobile_number_length(value: str):
    """
    Validates Mobile number always have a length of 10.
    """

    if len(value) != 10:
        raise ValidationError(
            f"The Mobile number must be 10 digits, you have entered {len(value)} digits."
        )


# """
# Validator for string that should contain only digits.
# """
string_only_contain_digits_validator = RegexValidator(
    regex=r'^[0-9]*$',
    message='Only digits are allowed in mobile number',
    code="invalid_numric_value"
)
