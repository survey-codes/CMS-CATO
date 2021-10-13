from infrastucture.dataaccess.main.inline.language_inline import LanguageInline
from infrastucture.dataaccess.contents.models import GeneralDataLanguage


class GeneralDataLanguageInline(LanguageInline):
    __FOOTER = "footer"

    suit_classes = 'suit-tab suit-tab-language'
    model = GeneralDataLanguage
    fields = (__FOOTER,)
