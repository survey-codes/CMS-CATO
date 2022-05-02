from infrastucture.main.inline.language_inline import LanguageInline
from infrastucture.contents.models import SectionLanguage
from infrastucture.constants import TITLE_KEY


class SectionLanguageInline(LanguageInline):
    __DESCRIPTION_KEY = "description"

    model = SectionLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (TITLE_KEY, __DESCRIPTION_KEY)
