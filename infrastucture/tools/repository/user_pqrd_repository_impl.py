from domain.main.tools.repository.user_pqrd_repository import UserPqrdRepository
from infrastucture.tools.acl.user_pqrd_acl import UserPqrdAcl
from infrastucture.tools.models import UserPqrd


class UserPqrdRepositoryImpl(UserPqrdRepository):
    __user_pqrd_acl = UserPqrdAcl()
    __user_pqrd = UserPqrd.objects

    def select(self):
        users_pqrd_model = self.__user_pqrd.filter(active=True)
        return self.__user_pqrd_acl.from_models_to_domains(users_pqrd_model)

    def select_by_ids(self, ids: list):
        users_pqrd_model = self.__user_pqrd.filter(active=True, pk__in=ids)
        return self.__user_pqrd_acl.from_models_to_domains(users_pqrd_model)

    def there_are_active_users(self):
        active_users = self.__user_pqrd.filter(active=True)
        return active_users.count() > 0

    # def create(self, email: str) -> Response:
    #     user_pqrd_model = UserPqrd.objects.create(email=email)
    #     user_pqrd_domain = self.__user_pqrd_acl.from_model_to_domain(user_pqrd_model)
    #     return Response(TypeResponse.SUCCESS ,user_pqrd_domain)
