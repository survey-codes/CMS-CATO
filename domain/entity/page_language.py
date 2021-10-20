from graphene import String, ObjectType, JSONString


class PageLanguage(ObjectType):
    language = String()
    title = String()
    description = String()
    metadata = JSONString()
