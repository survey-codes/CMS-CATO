ZERO_QUOTA = "You already spent all your quota."


class ZeroQuotaException(Exception):
    def __init__(self):
        super(ZeroQuotaException, self).__init__(ZERO_QUOTA)
