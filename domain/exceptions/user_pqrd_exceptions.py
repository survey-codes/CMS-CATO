from django.forms import ValidationError

DO_NOT_WRITE_EMAIL_ERROR = "Debes escribir un correo electrónico"


def do_not_write_email_exception():
    return ValidationError(DO_NOT_WRITE_EMAIL_ERROR)
