class EmptyNameException(Exception):
    MESSAGE = "Debes ingresar un nombre correctamente, por favor llena todos los campos!"

    def __init__(self):
        super(EmptyNameException, self).__init__(self.MESSAGE)
