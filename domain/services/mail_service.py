from domain.constants import DEFAULT_BOOL
from infrastucture.dataaccess.tools.models import Mail


class MailService:
    __mail = Mail.objects

    def select(self) -> 'Queryset[Mail]':
        return self.__mail.filter(active=DEFAULT_BOOL)

    def plus_amount(self, mail_pk, successful_amount):
        mail = self.select().filter(pk=mail_pk).first()
        mail.add_to_amount_send(successful_amount)
        mail.save()
