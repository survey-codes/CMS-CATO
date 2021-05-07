INVALID_FORM = "Lo sentimos, tenemos problemas con el formulario, intenta nuevamente"


class InvalidFromException(Exception):
    def __init__(self):
        super(InvalidFromException, self).__init__(INVALID_FORM)
