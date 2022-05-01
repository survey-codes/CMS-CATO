import os

from django.conf import settings
from sendgrid import Mail, SendGridAPIClient

from infrastucture.messengerservice.MessengerServiceInterface import MessengerServiceInterface
from infrastucture.messengerservice.model import MailDto


class MessengerServiceSendgrid(MessengerServiceInterface):
    __sendgrid = SendGridAPIClient(os.environ.get("API_KEY_SENDGRIP"))

    def send_mail(self, mail: MailDto):
        message = Mail(from_email=mail.from_email, to_emails=mail.to_emails, subject=mail.subject,
                       html_content=mail.content)
        response = self.__sendgrid.send(message)
        if settings.DEBUG:
            print(response.status_code)
            print(response.body)
            print(response.headers)
