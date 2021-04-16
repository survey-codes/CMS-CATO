from django.utils.translation import ugettext_lazy as _

EMPTY_TEMPLATE_MESSAGE = _("This mail does not have an associated template")


class EmptyTemplateException(Exception):
    def __init__(self):
        super(EmptyTemplateException, self).__init__(EMPTY_TEMPLATE_MESSAGE)
