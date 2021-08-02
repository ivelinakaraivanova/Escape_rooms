from django.core.exceptions import ValidationError


def validate_start_time(value):
    possible_start_hours = (10, 12, 14, 16, 18, 20)

    if value.hour not in possible_start_hours:
        raise ValidationError('Start hour should be within even hours from 10 to 20')
    if value.minute != 0 or value.second != 0 or value.microsecond != 0:
        raise ValidationError('Start time should be on the hour')   # TODO --> correct the message
    return value
