from django.forms import ValidationError

DO_NOT_SELECT_TYPE_ERROR = "Debes seleccionar un tipo para poder continuar"


def do_not_select_type_exception():
    return ValidationError(DO_NOT_SELECT_TYPE_ERROR)
