from adminsortable.admin import NonSortableParentAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from infrastucture.constants import LANGUAGE_TAB, MENU_KEY
from infrastucture.contents.inline.general_data_language_inline import GeneralDataLanguageInline
from infrastucture.contents.models import GeneralData
from infrastucture.main.admin.filter_date_admin import FilterDateAdmin
from infrastucture.utilities.image import Image


@admin.register(GeneralData)
class GeneralDataAdmin(NonSortableParentAdmin, FilterDateAdmin):
    __IMAGE_PREVIEW = _("Preview")
    __LOGO_PREVIEW = _('Logo')
    __LOGO_KEY = "logo"
    __GENERAL = _("General")

    list_display = (MENU_KEY, '_get_logo')
    inlines = [GeneralDataLanguageInline]
    fieldsets = (
        (__GENERAL, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (MENU_KEY, __LOGO_KEY, '_get_logo')
        }),
    )
    raw_id_fields = (MENU_KEY,)
    readonly_fields = ('_get_logo',)
    suit_form_tabs = (
        ('general', __GENERAL),
        ('language', LANGUAGE_TAB)
    )

    def _get_logo(self, obj):
        image = obj.logo
        return Image.get_image_preview(obj, img=image, title=self.__LOGO_PREVIEW)

    _get_logo.allow_tags = True
    _get_logo.short_description = __IMAGE_PREVIEW
