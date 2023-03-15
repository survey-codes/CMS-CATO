from infrastucture.messengerservice.model import MailDto


class MessengerServiceInterface:
    def send_mail(self, mail: MailDto):
        pass
