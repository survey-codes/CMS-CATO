from django.utils.translation import ugettext_lazy as _


class EmptyTemplateException(Exception):
    __MESSAGE = _("This mail does not have an associated template")

    def __init__(self):
        super(EmptyTemplateException, self).__init__(self.__MESSAGE)
