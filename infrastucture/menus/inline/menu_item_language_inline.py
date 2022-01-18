from infrastucture.constants import NAME_KEY
from infrastucture.main.inline.language_inline import LanguageInline
from infrastucture.menus.models.menu_item_language import MenuItemLanguage


class MenuItemLanguageInline(LanguageInline):
    model = MenuItemLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
