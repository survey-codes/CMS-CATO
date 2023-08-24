class SectionTemplate:
    pk = int
    name = str
    nickname = str
    preview = str

    def __init__(self, pk: property, name: str, nickname: str, preview: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.name = name
        self.nickname = nickname
        self.preview = preview
