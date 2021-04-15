from django.forms import ValidationError

DO_NOT_SELECT_TYPE_ERROR = "Debes seleccionar un tipo para poder continuar"


class DoNotSelectTypeException(ValidationError):
    def __init__(self):
        super(DoNotSelectTypeException, self).__init__(DO_NOT_SELECT_TYPE_ERROR)
