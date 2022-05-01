from celery.utils.log import get_logger

from domain.main.exceptions.zero_quota_exception import ZeroQuotaException
from domain.main.tools.services.mail_service import MailService
from domain.main.tools.services.quota_service import QuotaService
from domain.main.tools.services.user_pqrd_service_borrador import UserPqrdServiceBorrador
from domain.main.tools.valueobject.response_user_send import ResponseUserSend
from infrastucture.messengerservice.MessengerServiceInterface import MessengerServiceInterface
from infrastucture.messengerservice.model.MailDto import MailDto
from infrastucture.tools.repository.user_pqrd_repository_impl import UserPqrdRepositoryImpl

logger = get_logger(__name__)


class SendTask:

    __quota_service = QuotaService()
    __mail_service = MailService()
    __MAIL_KEY = "mail"

    def __init__(self, messenger_service: MessengerServiceInterface):
        self.__messenger_service = messenger_service
        self.__users_pqrd_repository_impl = UserPqrdRepositoryImpl()

    # @task(name=__MAIL_KEY)
    def mail(self, users_pk, mail_pk):
        users = self.__users_pqrd_repository_impl.select_by_ids(users_pk)
        response = self.__send_mail(users)
        self.__update_amount(mail_pk, response.successful_amount)

    def __send_mail(self, users):
        response = ResponseUserSend()
        for user in users:
            to_emails = [user.email]
            mailDto = MailDto(
                from_email='andres.diaz.velasquez@unillanos.edu.co',
                to_emails=to_emails,
                subject='Sending with Twilio SendGrid is Fun',
                content='<strong>and easy to do anywhere, even with Python</strong>'
            )
            try:
                self.__messenger_service.send_mail(mailDto)
                response.plus_one_successful_amount()
            except Exception as exception:
                response.plus_one_failed_amount()
                raise exception
        return response

    def __update_amount(self, mail_pk, successful_amount):
        self.__mail_service.plus_amount(mail_pk, successful_amount)
        self.__quota_service.less_amount(self.__MAIL_KEY, successful_amount)
