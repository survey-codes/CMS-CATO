from domain.main.contents.model.general import General
from domain.main.contents.repository.general_repository import GeneralRepository
from domain.main.contents.services.general_service import GeneralService
from infrastucture.dataaccess.contents.repository.general_repository_impl import GeneralRepositoryImpl


class GeneralPresenter:
    __general_service: GeneralService

    def __init__(self):
        general_repository: GeneralRepository = GeneralRepositoryImpl()
        self.__general_service = GeneralService(general_repository)

    def select(self, lang: str) -> General:
        return self.__general_service.select(lang)
