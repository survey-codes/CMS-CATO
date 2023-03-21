class EmptyValueException(Exception):
    MESSAGE = "Debes ingresar titulo correctamente, por favor llena todos los campos!"

    def __init__(self):
        super(EmptyValueException, self).__init__(self.MESSAGE)
