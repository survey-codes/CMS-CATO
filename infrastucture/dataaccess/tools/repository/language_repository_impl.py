from domain.entity.language import Language
from domain.repository.language_repository import LanguageRepository
from infrastucture.dataaccess.tools.acl.language_acl import LanguageAcl
from infrastucture.dataaccess.tools.models.language import Language as LanguageModel


class LanguageRepositoryImpl(LanguageRepository):
    __language_acl = LanguageAcl()

    def select(self) -> [Language]:
        languages = LanguageModel.objects.all()
        return self.__language_acl.from_list_model_to_list_domain(languages)

    def select_by_abbreviation(self, abbreviation: str) -> [Language]:
        languages_model = LanguageModel.objects.filter(abbreviation=abbreviation)
        assert languages_model, "Lo sentimos :( no encontramos un idiomas"
        return self.__language_acl.from_list_model_to_list_domain(languages_model)
