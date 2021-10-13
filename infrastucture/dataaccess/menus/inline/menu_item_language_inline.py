from infrastucture.dataaccess.menus.models.menu_item_language import MenuItemLanguage
from infrastucture.constants import NAME_KEY
from infrastucture.dataaccess.main.inline.language_inline import LanguageInline


class MenuItemLanguageInline(LanguageInline):
    model = MenuItemLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
