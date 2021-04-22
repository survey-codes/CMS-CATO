class ZeroQuotaException(Exception):
    __ZERO_QUOTA = "You already spent all your quota."

    def __init__(self):
        super(ZeroQuotaException, self).__init__(self.__ZERO_QUOTA)
