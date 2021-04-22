from domain.constants import DEFAULT_BOOL
from infrastructure.data_access.entities.tools.models import Quota


class QuotaService:
    __quota = Quota.objects.filter(active=DEFAULT_BOOL)

    def select_by_type(self, type_quota) -> Quota:
        return self.__quota.filter(type=type_quota).first()
