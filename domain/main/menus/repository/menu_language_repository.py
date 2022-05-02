from typing import Optional

from domain.main.menus.entity.menu_language import MenuLanguage


class MenuLanguageRepository:
    def select_by_menu_pk(self, menu_pk: property, lang: str) -> Optional[MenuLanguage]:
        pass
