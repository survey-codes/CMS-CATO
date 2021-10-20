from domain.entity.page_language import PageLanguage
from domain.repository.page_language_repository import PageLanguageRepository
from infrastucture.dataaccess.contents.acl.page_language_acl import PageLanguageAcl
from infrastucture.dataaccess.contents.models.pages import PageLanguage as PageLanguageModel


class PageLanguageRepositoryImpl(PageLanguageRepository):
    __page_language_acl = PageLanguageAcl()

    def select_by_page_pk(self, page_pk: property, lang: str) -> PageLanguage:
        language_model = PageLanguageModel.objects.filter(page__pk=page_pk, language__abbreviation=lang).first()
        return self.__page_language_acl.from_model_to_domain(language_model)
