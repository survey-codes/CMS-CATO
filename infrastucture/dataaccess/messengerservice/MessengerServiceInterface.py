from infrastucture.dataaccess.messengerservice.model import MailDto


class MessengerServiceInterface:
    def send_mail(self, mail: MailDto):
        pass
