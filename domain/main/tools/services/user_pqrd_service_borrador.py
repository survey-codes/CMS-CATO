from domain.main.constants import DEFAULT_BOOL
from infrastucture.dataaccess.tools.models import UserPqrd


class UserPqrdServiceBorrador:
    __user_pqrd = UserPqrd.objects

    def select(self) -> 'Queryset[UserPqrd]':
        return self.__user_pqrd.filter(active=DEFAULT_BOOL)

    def select_by_list(self, ids: str) -> 'Queryset[UserPqrd]':
        ids_list = ids.split(",")
        return self.select().filter(pk__in=ids_list)

    def select_by_ids(self, ids: list) -> 'Queryset[UserPqrd]':
        return self.select().filter(pk__in=ids)
