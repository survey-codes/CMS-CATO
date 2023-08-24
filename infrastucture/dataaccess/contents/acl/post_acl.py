from typing import Optional

from domain.main.contents.model.post import Post as PostDomain
from infrastucture.dataaccess.contents.models import Post as PostModel, PostLanguage


class PostAcl:
    @staticmethod
    def from_model_to_domain(model: PostModel, lang: str) -> Optional[PostDomain]:
        language: PostLanguage = model.translations.filter(language__abbreviation=lang).first()
        title = None
        if language:
            title = language.title
        logo = model.logo
        logo_path = None
        if logo:
            logo_path = logo.url
        icon = model.icon
        icon_path = None
        if icon:
            icon_path = icon.url
        link = model.link
        slug = model.slug
        return PostDomain(model.pk, title, logo_path, icon_path, link, slug)

    def from_model_list_to_domain_list(self, model_list: [PostModel], lang: str) -> [PostDomain]:
        return map(lambda model: self.from_model_to_domain(model, lang), model_list)
