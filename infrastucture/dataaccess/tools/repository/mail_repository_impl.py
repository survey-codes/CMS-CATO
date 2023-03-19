from domain.main.tools.repository.mail_repository import MailRepository
from infrastucture.dataaccess.tools.models import Mail


class MailRepositoryImpl(MailRepository):
    __mail = Mail.objects

    def increase_amount(self, id, amount):
        mail = self.__mail.filter(pk=id).first()
        new_amount = mail.amount_send + amount
        mail.amount_send = new_amount
        mail.save()


    def isEmpty(self):
        return self.__mail.count() == 0
