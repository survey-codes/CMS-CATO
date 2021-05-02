from cms.infrastructure.data_access.entities.contents.models import PageLanguage
from cms.presentation.constants import TITLE_KEY
from cms.presentation.main.inline.language_inline import LanguageInline


class PageLanguageInline(LanguageInline):
    __DESCRIPTION_KEY = "description"

    model = PageLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (TITLE_KEY, __DESCRIPTION_KEY)
