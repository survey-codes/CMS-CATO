from django.utils.translation import ugettext_lazy as _

SUCCESSFUL_SHIPMENT = _("We send the message to {} users.")
FAILED_SHIPMENT = _("We send the message to {} users.")


class ResponseUserSend(object):
    successful_amount = 0
    failed_amount = 0
    users_successful = list()
    users_failed = list()

    def plus_one_successful_amount(self):
        self.successful_amount += 1

    def plus_one_failed_amount(self):
        self.failed_amount += 1

    def message_successful_shipment(self):
        return SUCCESSFUL_SHIPMENT.format(self.successful_amount)

    def message_failed_shipment(self):
        return FAILED_SHIPMENT.format(self.failed_amount)

    def add_user(self, user):
        self.users_successful.append(user)
        self.plus_one_successful_amount()

    def __str__(self):
        return f"successful_amount: {self.successful_amount}, failed_amount: {self.failed_amount}"
