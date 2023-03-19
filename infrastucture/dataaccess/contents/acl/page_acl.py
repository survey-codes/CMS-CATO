from typing import Optional

from domain.main.contents.model.page import Page as PageDomain
from infrastucture.dataaccess.contents.models import Page as PageModel, PageLanguage


class PageAcl:

    @staticmethod
    def from_model_to_domain(model: PageModel, lang: str) -> Optional[PageDomain]:
        language: PageLanguage = model.translations.filter(language__abbreviation=lang).first()
        if language:
            pk = int(model.pk)
            title = language.title
            description = language.description
            metadata = language.metadata
            children = []
            return PageDomain(
                pk=pk,
                title=title,
                description=description,
                metadata=metadata,
                children=children,
                order=model.order,
                slug=model.slug
            )
        return None

    def from_models_to_domains(self, models: [PageModel], lang: str) -> [PageDomain]:
        domains = map(lambda model: self.from_model_to_domain(model, lang), models)
        return list(filter(lambda domain: domain is not None, domains))
