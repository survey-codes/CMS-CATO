from domain.main.common.aggregate.response import Response
from domain.main.exceptions.empty_mail_exception import EmptyMailException
from domain.main.tools.repository.user_pqrd_repository import UserPqrdRepository


class UserPqrdService:
    def __init__(self, user_pqrd_repository: UserPqrdRepository):
        self.__user_pqrd_repository = user_pqrd_repository

    def create(self, email: str) -> Response:
        if not email:
            raise EmptyMailException()
        # return self.__user_pqrd_repository.create(email)
