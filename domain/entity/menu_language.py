from graphene import ObjectType, String


class MenuLanguage(ObjectType):
    language = String()
    name = String()
    metadata = String()

    def __init__(self, language: str, name: str, metadata: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = language
        self.name = name
        self.metadata = metadata
