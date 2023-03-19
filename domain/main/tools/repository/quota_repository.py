from infrastucture.dataaccess.tools.models import QuotaType


class QuotaRepository:

    def haveQuotaByType(self, quota_type: QuotaType):
        pass

    def less_amount(self, amount, quota_type: QuotaType):
        pass

    def select(self):
        pass
