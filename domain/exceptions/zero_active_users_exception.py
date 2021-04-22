class ZeroActiveUsersException(Exception):
    __MESSAGE = "No pudimos completar la solicitud, debido a que no hay usuarios activos :("

    def __init__(self):
        super(ZeroActiveUsersException, self).__init__(self.__MESSAGE)
