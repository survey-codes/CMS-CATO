from domain.main.contents.model.general import General
from infrastucture.dataaccess.contents.models import GeneralData, GeneralDataLanguage
from infrastucture.dataaccess.menus.acl.menu_acl import MenuAcl


class GeneralAcl:
    __menu_acl = MenuAcl()

    def from_model_to_domain(self, model: GeneralData, lang: str) -> General:
        language: GeneralDataLanguage = model.translations.filter(language__abbreviation=lang).first()
