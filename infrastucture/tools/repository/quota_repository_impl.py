from domain.main.tools.repository.quota_repository import QuotaRepository
from infrastucture.constants import MAIL_KEY
from infrastucture.tools.models import Quota
from infrastucture.tools.models.quota_type import QuotaType


class QuotaRepositoryImpl(QuotaRepository):
    __quota = Quota.objects

    def haveQuotaByType(self, quota_type: QuotaType):
        quota = self.__quota.filter(type__contains=quota_type.value).first()
        return quota and quota.amount > 0

    def less_amount(self, amount, quota_type: QuotaType):
        quota = self.__quota.filter(type__contains=quota_type.value).first()
        new_amount = quota.amount - amount
        quota.amount = self.__validate_amount(new_amount)
        quota.save()

    @staticmethod
    def __validate_amount(amount) -> int:
        if amount < 0:
            return 0
        return amount

    def select(self):
        return self.__quota.filter(type__contains=MAIL_KEY).first()
