class ZeroActiveUsersException(Exception):
    __NO_ACTIVE_USERS = "No pudimos completar la solicitud, debido a que no hay usuarios activos :("

    def __init__(self):
        super(ZeroActiveUsersException, self).__init__(self.__NO_ACTIVE_USERS)
