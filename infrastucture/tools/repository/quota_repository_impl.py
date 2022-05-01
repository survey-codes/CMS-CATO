from infrastucture.constants import MAIL_KEY
from infrastucture.tools.models import Quota
from infrastucture.tools.models.quota_type import QuotaType


class QuotaRepositoryImpl:
    __quota = Quota.objects

    def haveQuotaByType(self, quota_type: QuotaType):
        quota = self.__quota.filter(type__contains=quota_type.value).first()
        return quota and quota.amount > 0

    def select(self):
        return self.__quota.filter(type__contains=MAIL_KEY).first()
