from typing import Optional

from domain.main.contents.model.page import Page as PageDomain
from infrastucture.dataaccess.contents.models import Page as PageModel, PageLanguage
from infrastucture.dataaccess.menus.acl.menu_acl import MenuAcl


class PageAcl:
    __menu_acl = MenuAcl()

    def from_model_to_domain(self, model: PageModel, lang: str) -> Optional[PageDomain]:
        language: PageLanguage = model.translations.filter(language__abbreviation=lang).first()
        menu = model.menu
        if not language:
            return None
        title = language.title
        description = language.description
        metadata = language.metadata
        children = []
        menu = self.__menu_acl.from_model_to_domain(menu, lang)
        return PageDomain(
            pk=model.pk,
            title=title,
            description=description,
            metadata=metadata,
            children=children,
            order=model.order,
            slug=model.slug,
            menu=menu
        )

    def from_models_to_domains(self, models: [PageModel], lang: str) -> [PageDomain]:
        domains = map(lambda model: self.from_model_to_domain(model, lang), models)
        return list(filter(lambda domain: domain is not None, domains))
