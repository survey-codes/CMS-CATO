class EmptyMailException(Exception):
    __MESSAGE = "Lo sentimos, aun no has creado correos"

    def __init__(self):
        super(EmptyMailException, self).__init__(self.__MESSAGE)
