from domain.main.contents.model.page_language import PageLanguage
from domain.main.contents.repository.page_language_repository import PageLanguageRepository
from infrastucture.dataaccess.contents.acl.page_language_acl import PageLanguageAcl
from infrastucture.dataaccess.contents.models import PageLanguage as PageLanguageModel


class PageLanguageRepositoryImpl(PageLanguageRepository):
    __page_language_acl = PageLanguageAcl()

    def select(self, lang: str, slug: str) -> [PageLanguage]:
        languages_model = PageLanguageModel.objects.filter(language__abbreviation=lang, page__slug=slug)
        return self.__page_language_acl.from_models_to_domains(languages_model)

    def select_by_page_pk(self, page_pk: property, lang: str) -> PageLanguage:
        language_model = PageLanguageModel.objects.filter(page__pk=page_pk, language__abbreviation=lang).first()
        return self.__page_language_acl.from_model_to_domain(language_model)
