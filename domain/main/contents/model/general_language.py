from graphene import ObjectType, String, JSONString, Int

from domain.main.exceptions.general.empty_metadata_exception import EmptyMetadataException


class GeneralDataLanguage(ObjectType):
    pk = Int()
    footer = String()
    metadata = JSONString()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__validate_fields()

    def __validate_fields(self):
        self.__is_metadata_empty()

    def __is_metadata_empty(self):
        if not self.metadata:
            raise EmptyMetadataException()
