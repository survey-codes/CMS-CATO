from graphene import ObjectType, String

from domain.main.exceptions.empty_mail_exception import EmptyMailException


class UserPqrd(ObjectType):
    email = String()

    def __init__(self, *args, **kwargs):
        super(UserPqrd, self).__init__(*args, **kwargs)
        self.__validate_fields()

    def __validate_fields(self):
        if not self.email:
            raise EmptyMailException()
