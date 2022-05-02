from domain.main.common.aggregate.response import Response
from domain.main.tools.repository.user_pqrd_repository import UserPqrdRepository
from domain.main.tools.services.user_pqrd_service import UserPqrdService
from infrastucture.tools.repository.user_pqrd_repository_impl import UserPqrdRepositoryImpl


class UserPqrdPresenter:
    def __init__(self):
        user_pqrd_repository: UserPqrdRepository = UserPqrdRepositoryImpl()
        self.__user_pqrd_service = UserPqrdService(user_pqrd_repository)

    def create(self, email: str) -> Response:
        return self.__user_pqrd_service.create(email)
