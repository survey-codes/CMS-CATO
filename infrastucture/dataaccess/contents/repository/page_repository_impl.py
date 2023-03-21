from domain.main.contents.model.page import Page as PageDomain
from domain.main.contents.repository.page_repository import PageRepository
from infrastucture.dataaccess.contents.acl.page_acl import PageAcl
from infrastucture.dataaccess.contents.acl.page_language_acl import PageLanguageAcl
from infrastucture.dataaccess.contents.models import Page as PageModel


class PageRepositoryImpl(PageRepository):
    __page_acl = PageAcl()
    __page_language_acl = PageLanguageAcl()

    def select(self, lang: str, slug: str) -> [PageDomain]:
        pages_model: [PageModel]
        if slug:
            pages_model = PageModel.objects.filter(slug=slug)
        else:
            pages_model = PageModel.objects.all()
        return self.__page_acl.from_models_to_domains(pages_model, lang)

    def select_children_by_pk(self, pk: property) -> [int]:
        children = PageModel.objects.filter(parent__pk=pk)
        return map(lambda child: child.pk, children)
