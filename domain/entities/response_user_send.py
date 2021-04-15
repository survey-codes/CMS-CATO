from django.utils.translation import ugettext_lazy as _

SUCCESSFUL_SHIPMENT = _("We send the message to {} users.")
FAILED_SHIPMENT = _("We send the message to {} users.")


class ResponseUserSend:
    successful_amount = 0
    failed_amount = 0
    users_failed = None

    def plus_one_successful_amount(self):
        self.successful_amount += 1

    def plus_one_failed_amount(self):
        self.failed_amount += 1

    def message_successful_shipment(self):
        return SUCCESSFUL_SHIPMENT.format(self.successful_amount)

    def message_failed_shipment(self):
        return FAILED_SHIPMENT.format(self.failed_amount)

    def has_failed_users(self):
        return self.failed_amount > 0
