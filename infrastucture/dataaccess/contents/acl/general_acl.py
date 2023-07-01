from domain.main.contents.model.general import General
from infrastucture.dataaccess.contents.models import GeneralData, GeneralDataLanguage
from infrastucture.dataaccess.menus.acl.menu_acl import MenuAcl


class GeneralAcl:
    __menu_acl = MenuAcl()

    def from_model_to_domain(self, model: GeneralData, lang: str) -> General:
        pk = None
        menu = None
        image_path = ""
        footer_rich_text = ""
        if model:
            pk = model.pk
            language = model.translations.filter(language__abbreviation=lang).first()
            menu = self.__menu_acl.from_model_to_domain(model=model.menu, lang=lang)
            if model.logo:
                image_path = model.logo.path
            if language:
                footer_rich_text = language.footer
        return General(
            pk=pk,
            image=image_path,
            footer=footer_rich_text,
            menu=menu
        )
