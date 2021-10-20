from domain.entity.page_language import PageLanguage as PageLanguageDomain
from domain.repository.page_language_repository import PageLanguageRepository
from infrastucture.dataaccess.contents.acl.page_language_acl import PageLanguageAcl
from infrastucture.dataaccess.contents.models import PageLanguage as PageLanguageModel


class PageLanguageRepositoryImpl(PageLanguageRepository):
    __page_language_acl = PageLanguageAcl()

    def select(self, lang: str, slug: str) -> [PageLanguageDomain]:
        models = PageLanguageModel.objects.filter(language__abbreviation=lang, page__slug=slug)
        assert models, "No se encontraron páginas, por favor intenta nuevamente"
        return self.__page_language_acl.from_models_to_domains(models)
