class MenuItem:
    pk: int
    name: str
    link: str
    sub_item: 'MenuItem'

    def __init__(self, pk: property, name: str, link: str, sub_item: 'MenuItem', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.name = name
        self.link = link
        self.sub_item = sub_item

    def __str__(self):
        return f"{{ pk: {self.pk}, name: {self.name}, link: {self.link} }}"
