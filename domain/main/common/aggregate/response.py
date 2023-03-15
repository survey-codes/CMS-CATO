from graphene import ObjectType

from domain.main.common.valueobject.type_response import TypeResponse


class Response(ObjectType):

    def __init__(self, type_response: TypeResponse, entity: ObjectType, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_response = type_response
        self.entity = entity
