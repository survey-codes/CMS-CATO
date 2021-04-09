from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


PREVIEW_TEXT = _("(Choose an image and save for continue editing and see the preview)")


def get_image_preview(obj, img, title, width=100, field_msg=PREVIEW_TEXT):
    if obj.pk:
        return mark_safe(f"""<a href="{img}" target="_blank">
        <img src="{img}" alt="{title}" style="max-width:{width}px; height: auto;" /></a>""")
    return field_msg
