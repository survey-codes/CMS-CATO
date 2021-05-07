from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.presentation.constants import EMPTY_VALUE


class Image:
    PREVIEW_TEXT = _("(Choose an image and save for continue editing and see the preview)")

    @staticmethod
    def get_image_preview(obj, img, title, width=100, field_msg=PREVIEW_TEXT):
        if obj.pk:
            if img:
                url = img.url
                return mark_safe(f"""<a href="{url}" target="_blank">
                <img src="{url}" alt="{title}" style="max-width:{width}px; height: auto;" /></a>""")
            return EMPTY_VALUE
        return field_msg
