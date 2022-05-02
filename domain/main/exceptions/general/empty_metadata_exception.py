class EmptyMetadataException(Exception):
    MESSAGE = "Debes ingresar metadata correctamente, por favor llena todos los campos!"

    def __init__(self):
        super(EmptyMetadataException, self).__init__(self.MESSAGE)
