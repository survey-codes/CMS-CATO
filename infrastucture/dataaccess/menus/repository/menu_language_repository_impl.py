from typing import Optional

from domain.main.menus.entity.menu_language import MenuLanguage as MenuLanguageDomain
from domain.main.menus.repository.menu_language_repository import MenuLanguageRepository
from infrastucture.dataaccess.menus.acl.menu_language_acl import MenuLanguageAcl
from infrastucture.dataaccess.menus.models.menu_language import MenuLanguage as MenuLanguageModel


class MenuLanguageRepositoryImpl(MenuLanguageRepository):
    __menu_language_acl = MenuLanguageAcl()

    def select_by_menu_pk(self, menu_pk: property, lang: str) -> Optional[MenuLanguageDomain]:
        language = MenuLanguageModel.objects.filter(menu__pk=menu_pk, language__abbreviation=lang).first()
        return self.__menu_language_acl.from_model_to_domain(language)
