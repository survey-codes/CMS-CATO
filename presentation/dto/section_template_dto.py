from graphene import ObjectType, Int, String


class SectionTemplateDto(ObjectType):
    pk = Int()
    name = String()
    nickname = String()
    preview = String()

    def __init__(self, pk: int, name: str, nickname: str, preview: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.name = name
        self.nickname = nickname
        self.preview = preview


