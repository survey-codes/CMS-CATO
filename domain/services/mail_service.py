from domain.constants import DEFAULT_BOOL
from infrastructure.data_access.entities.tools.models import Mail


class MailService:
    __mail = Mail.objects.filter(active=DEFAULT_BOOL)

    def select(self) -> 'Queryset[Mail]':
        return self.__mail