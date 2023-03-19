from domain.main.contents.entity.page import Page as PageDomain
from infrastucture.dataaccess.contents.models import Page as PageModel


class PageAcl:

    @staticmethod
    def from_model_to_domain(model: PageModel) -> PageDomain:
        return PageDomain(pk=model.pk, order=model.order, slug=model.slug)

    def from_models_to_domains(self, models: [PageModel]) -> [PageDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
