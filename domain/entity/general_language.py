from graphene import ObjectType, String, JSONString

from domain.exceptions.general.empty_metadata_exception import EmptyMetadataException


class GeneralLanguage(ObjectType):
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
