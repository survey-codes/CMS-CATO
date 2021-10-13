from domain.constants import DEFAULT_BOOL
from infrastucture.dataaccess.tools.models import Quota


class QuotaService:
    __quota = Quota.objects.filter(active=DEFAULT_BOOL)

    def select_by_type(self, type_quota) -> Quota:
        return self.__quota.filter(type=type_quota).first()

    def less_amount(self, type, successful_amount):
        quota = self.__quota.filter(type=type).first()
        quota.subtract_quota(successful_amount)
        quota.save()

    def have_quota(self, type):
        quota = self.__quota.filter(type=type).first()
        return quota.amount > 0
