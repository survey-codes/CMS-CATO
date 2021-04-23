from infrastructure.data_access.entities.contents.models.extra import GeneralDataLanguage
from presentation.main.inline.language_inline import LanguageInline


class GeneralDataLanguageInline(LanguageInline):
    __FOOTER = "footer"

    suit_classes = 'suit-tab suit-tab-language'
    model = GeneralDataLanguage
    fields = (__FOOTER,)
