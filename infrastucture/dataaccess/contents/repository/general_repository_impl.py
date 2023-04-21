from domain.main.contents.model.general import General as GeneralDomain
from domain.main.contents.repository.general_repository import GeneralRepository
from infrastucture.dataaccess.contents.acl.general_acl import GeneralAcl
from infrastucture.dataaccess.contents.models import GeneralData


class GeneralRepositoryImpl(GeneralRepository):
    __general_acl = GeneralAcl()

    def select(self, lang: str) -> GeneralDomain:
        general_model = GeneralData.objects.first()
        return self.__general_acl.from_model_to_domain(general_model, lang)
