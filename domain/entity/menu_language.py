from graphene import ObjectType, String


class MenuLanguage(ObjectType):
    language = String()
    name = String()
    metadata = String()
