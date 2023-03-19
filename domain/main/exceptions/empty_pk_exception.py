class BadPkException(Exception):
    __MESSAGE = "Lo sentimos, no podemos continuar con la busqueda sin un ID"

    def __init__(self):
        super(BadPkException, self).__init__(self.__MESSAGE)
