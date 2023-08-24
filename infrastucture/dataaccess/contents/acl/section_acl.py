from typing import Optional

from domain.main.contents.model.section import Section as SectionDomain
from infrastucture.dataaccess.contents.acl.post_acl import PostAcl
from infrastucture.dataaccess.contents.acl.section_template_acl import SectionTemplateAcl
from infrastucture.dataaccess.contents.models import Section as SectionModel, SectionLanguage


class SectionAcl:
    __section_template_acl = SectionTemplateAcl()
    __post_acl = PostAcl()

    def from_model_to_domain(self, model: SectionModel, lang: str) -> Optional[SectionDomain]:
        language: SectionLanguage = model.translations.filter(language__abbreviation=lang).first()
        title = None
        description = None
        if language:
            title = language.title
            description = language.description
        background_url = None
        if model.background:
            background_url = model.background.url
        color = str(model.background_color)
        templates = self.__section_template_acl.from_model_to_domain(model.template)
        posts = self.__post_acl.from_model_list_to_domain_list(model.posts.all(), lang)
        return SectionDomain(model.pk, title, description, background_url, color, templates, model.slug,
                             model.order, model.align, posts)

    def from_model_list_to_domain_list(self, model_list: [SectionModel], lang: str) -> [SectionDomain]:
        return map(lambda model: self.from_model_to_domain(model, lang), model_list)
