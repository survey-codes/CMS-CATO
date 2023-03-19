from infrastucture.dataaccess.menus.models.menu_language import MenuLanguage
from infrastucture.constants import NAME_KEY
from infrastucture.dataaccess.main.inline import LanguageInline


class MenuLanguageInline(LanguageInline):
    model = MenuLanguage
    suit_classes = 'suit-tab suit-tab-language'
    fields = (NAME_KEY,)
