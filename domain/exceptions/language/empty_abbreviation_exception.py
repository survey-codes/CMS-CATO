class EmptyAbbreviationException(Exception):
    MESSAGE = "Debes ingresar una abreviación correcta, por favor llena todos los campos!"

    def __init__(self):
        super(EmptyAbbreviationException, self).__init__(self.MESSAGE)
