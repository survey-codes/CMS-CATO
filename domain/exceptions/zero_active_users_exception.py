NO_ACTIVE_USERS = "No pudimos completar la solicitud, debido a que no hay usuarios activos :("


class ZeroActiveUsersException(Exception):
    def __init__(self):
        super(ZeroActiveUsersException, self).__init__(NO_ACTIVE_USERS)
