from infrastucture.menus.models.menu_language import MenuLanguage
from infrastucture.constants import NAME_KEY
from infrastucture.main.inline.language_inline import LanguageInline


class MenuLanguageInline(LanguageInline):
    model = MenuLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
