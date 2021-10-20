from domain.entity.general_language import GeneralDataLanguage as GeneralDataLanguageDomain
from domain.repository.general_language_repository import GeneralDataLanguageRepository
from infrastucture.dataaccess.contents.acl.general_data_language_acl import GeneralDataLanguageAcl
from infrastucture.dataaccess.contents.models import GeneralDataLanguage


class GeneralDataLanguageRepositoryImpl(GeneralDataLanguageRepository):
    __general_data_acl = GeneralDataLanguageAcl()

    def select(self, lang: str) -> [GeneralDataLanguageDomain]:
        generals = GeneralDataLanguage.objects.filter(language__abbreviation=lang)
        return self.__general_data_acl.from_models_to_domains(generals)
