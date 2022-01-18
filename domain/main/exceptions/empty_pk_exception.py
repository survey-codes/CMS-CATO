class EmptyPkException(Exception):
    __MESSAGE = "Lo sentimos, no podemos continuar con la busqueda sin un ID"

    def __init__(self):
        super(EmptyPkException, self).__init__(self.__MESSAGE)
