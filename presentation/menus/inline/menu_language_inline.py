from infrastructure.data_access.entities.menus.menu_language import MenuLanguage
from presentation.constants import NAME_KEY
from presentation.main.inline.language_inline import LanguageInline


class MenuLanguageInline(LanguageInline):
    model = MenuLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
