from domain.constants import DEFAULT_BOOL
from infrastructure.data_access.entities.tools.models import UserPqrd


class UserPqrdService:
    __user_pqrd = UserPqrd.objects

    def select(self) -> 'Queryset[UserPqrd]':
        return self.__user_pqrd.filter(active=DEFAULT_BOOL)

    def select_by_list(self, ids: str) -> 'Queryset[UserPqrd]':
        ids_list = ids.split(",")
        return self.select().filter(pk__in=ids_list)
