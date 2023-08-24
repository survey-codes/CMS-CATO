from domain.main.contents.model.post import Post
from domain.main.contents.model.section_template import SectionTemplate


class Section:
    pk = int
    title = str
    description = str
    background = str
    background_color = str
    template = [SectionTemplate]
    slug = str
    order = int
    align = str
    posts = [Post]

    def __init__(
        self,
        pk: property,
        title: str,
        description: str,
        background: str,
        background_color: str,
        template: [SectionTemplate],
        slug: str,
        order: int,
        align: str,
        posts: [Post],
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.title = title
        self.description = description
        self.background = background
        self.background_color = background_color
        self.template = template
        self.slug = slug
        self.order = order
        self.align = align
        self.posts = posts
