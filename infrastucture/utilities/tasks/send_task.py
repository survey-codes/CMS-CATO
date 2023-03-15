from celery.utils.log import get_logger

from domain.main.tools.repository.mail_repository import MailRepository
from domain.main.tools.repository.quota_repository import QuotaRepository
from domain.main.tools.repository.user_pqrd_repository import UserPqrdRepository
from domain.main.tools.services.mail_service import MailService
from domain.main.tools.services.quota_service import QuotaService
from domain.main.tools.valueobject.response_user_send import ResponseUserSend
from infrastucture.messengerservice.MessengerServiceInterface import MessengerServiceInterface
from infrastucture.messengerservice.model.MailDto import MailDto
from infrastucture.tools.models.quota_type import QuotaType
from infrastucture.tools.repository.mail_repository_impl import MailRepositoryImpl
from infrastucture.tools.repository.quota_repository_impl import QuotaRepositoryImpl
from infrastucture.tools.repository.user_pqrd_repository_impl import UserPqrdRepositoryImpl

logger = get_logger(__name__)


class SendTask:
    __quota_service = QuotaService()
    __mail_service = MailService()
    __MAIL_KEY = "mail"

    def __init__(self, messenger_service: MessengerServiceInterface):
        self.__users_pqrd_repository: UserPqrdRepository = UserPqrdRepositoryImpl()
        self.__quota_repository: QuotaRepository = QuotaRepositoryImpl()
        self.__mail_repository: MailRepository = MailRepositoryImpl()
        self.__messenger_service = messenger_service

    # @task(name=__MAIL_KEY)
    def mail(self, users_pk, mail_pk):
        users = self.__users_pqrd_repository.select_by_ids(users_pk)
        response = self.__send_mail(users)
        self.__mail_repository.increase_amount(mail_pk, response.successful_amount)
        self.__quota_repository.less_amount(response.successful_amount, QuotaType.MAIL)

    def __send_mail(self, users):
        response = ResponseUserSend()
        for user in users:
            to_emails = [user.email]
            mail_dto = MailDto(
                from_email='andres.diaz.velasquez@unillanos.edu.co',
                to_emails=to_emails,
                subject='Sending with Twilio SendGrid is Fun',
                content='<strong>and easy to do anywhere, even with Python</strong>'
            )
            try:
                self.__messenger_service.send_mail(mail_dto)
                response.plus_one_successful_amount()
            except Exception as exception:
                response.plus_one_failed_amount()
                raise exception
        return response
