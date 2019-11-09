from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator


def validate_link(value):
    try:
        validate = URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
        validate(value)
    except ValidationError:
        raise ValidationError(
            _('Not a valid URL'),
            params={'value': value},
        )