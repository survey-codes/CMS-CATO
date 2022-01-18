class ItIsNotCapitalizedException(Exception):
    MESSAGE = "Este valor debe estar en mayuscula!"

    def __init__(self):
        super(ItIsNotCapitalizedException, self).__init__(self.MESSAGE)
