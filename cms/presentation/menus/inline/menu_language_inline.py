from cms.infrastructure.data_access.entities.menus.menu_language import MenuLanguage
from cms.presentation.constants import NAME_KEY
from cms.presentation.main.inline.language_inline import LanguageInline


class MenuLanguageInline(LanguageInline):
    model = MenuLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
