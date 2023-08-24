from typing import Optional

from domain.main.contents.model.section_template import SectionTemplate as SectionTemplateDomain
from infrastucture.dataaccess.contents.models import SectionTemplate as SectionTemplateModel


class SectionTemplateAcl:
    @staticmethod
    def from_model_to_domain(model: SectionTemplateModel) -> Optional[SectionTemplateDomain]:
        preview = ""
        if model.preview:
            preview = model.preview.url
        return SectionTemplateDomain(model.pk, model.name, model.nickname, preview)
