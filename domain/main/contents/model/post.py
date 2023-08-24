class Post:
    pk = int
    title = str
    logo = str
    icon = str
    link = str
    slug = str

    def __init__(self, pk: property, title: str, logo: str, icon: str, link: str, slug: str, *args,
                 **kwargs):
        super().__init__(args, kwargs)
        self.pk = pk
        self.title = title
        self.logo = logo
        self.icon = icon
        self.link = link
        self.slug = slug
