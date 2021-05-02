from cms.infrastructure.data_access.entities.menus.menu_item_language import MenuItemLanguage
from cms.presentation.constants import NAME_KEY
from cms.presentation.main.inline.language_inline import LanguageInline


class MenuItemLanguageInline(LanguageInline):
    model = MenuItemLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
