from celery.utils.log import get_logger

from domain.main.exceptions.zero_quota_exception import ZeroQuotaException
from domain.main.tools.services.mail_service import MailService
from domain.main.tools.services.quota_service import QuotaService
from domain.main.tools.services.user_pqrd_service import UserPqrdService
from domain.main.tools.valueobject.response_user_send import ResponseUserSend

logger = get_logger(__name__)


class SendTask:
    __users_pqrd_service = UserPqrdService()
    __quota_service = QuotaService()
    __mail_service = MailService()
    __MAIL_KEY = "mail"

    def __go_through_users(self, users):
        response = ResponseUserSend()
        for user in users:
            if not self.__quota_service.have_quota(self.__MAIL_KEY):
                raise ZeroQuotaException()
            try:
                print(f"Send mail to {user}")
                response.add_user(user)
            except Exception as exception:
                print(f"Not send mail to {user}")
                response.plus_one_failed_amount()
        return response

    def __update_amount(self, mail_pk, successful_amount):
        self.__mail_service.plus_amount(mail_pk, successful_amount)
        self.__quota_service.less_amount(self.__MAIL_KEY, successful_amount)

    # @task(name=__MAIL_KEY)
    def mail(self, users_pk, mail_pk):
        users = self.__users_pqrd_service.select_by_ids(users_pk)
        response = self.__go_through_users(users)
        self.__update_amount(mail_pk, response.successful_amount)
        print(response)
