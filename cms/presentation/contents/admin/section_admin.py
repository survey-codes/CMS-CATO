from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.domain.utilities.image import Image
from cms.infrastructure.data_access.entities.contents.models.sections import Section
from cms.presentation.constants import LANGUAGE_TAB, NO_PAGES, IMAGE_PREVIEW, TITLE_KEY, SLUG_KEY
from cms.presentation.contents.admin import PostSettingsInline
from cms.presentation.contents.inline.section_language_inline import SectionLanguageInline
from cms.presentation.main.admin.filter_date_admin import FilterDateAdmin


@admin.register(Section)
class SectionAdmin(FilterDateAdmin):
    __SECTION = _('Section')
    __POST_SETTINGS_PLURAL = _("Posts Settings")
    __VISIBILITY_HELP_TEXT = _('Check the box if the posts component is visible in this section')
    __CHOOSE_POSTS = _('Order posts')
    __SECTION_BACKGROUND_COLOR = _("Section background color")
    __SHOW_PAGES_SECTION = _('Pages in which appears ')
    __NO_POSTS = _("It has no posts")
    __POSTS = _('Posts')
    __TEMPLATE_KEY = "template"
    __ALIGN_KEY = "align"

    list_display = (TITLE_KEY, '_background_preview', '_background_color', '_show_pages', '_show_posts')
    actions = ['update_json_content']
    inlines = [SectionLanguageInline, PostSettingsInline, ]
    readonly_fields = ('slug', '_background_preview',)
    fieldsets = (
        (__SECTION, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (TITLE_KEY, 'background', '_background_preview', 'background_color', SLUG_KEY)
        }),
        (__POST_SETTINGS_PLURAL, {
            'classes': ('wide', 'suit-tab suit-tab-general'),
            'description': __VISIBILITY_HELP_TEXT,
            'fields': (__TEMPLATE_KEY, __ALIGN_KEY)
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
        ('language', LANGUAGE_TAB),
        ('post_settings', __CHOOSE_POSTS),
    )

    def _background_color(self, obj):
        background = obj.background_color
        if background:
            return mark_safe(f'<div style="background-color:{background}; height:50px; width: 50px"></div>')

    _background_color.short_description = __SECTION_BACKGROUND_COLOR

    def _show_pages(self, obj):
        pages = obj.pages.all()
        html = ""
        if pages:
            for page in pages:
                html += f'<li><a href="/admin/contents/page/{page.id}/">{page}</a></li>'
                return mark_safe(f'<ul>{html}</ul>')
        return NO_PAGES

    _show_pages.short_description = __SHOW_PAGES_SECTION

    def _background_preview(self, obj):
        image = obj.background
        if image:
            return Image.get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW, )

    _background_preview.allow_tags = True
    _background_preview.short_description = IMAGE_PREVIEW

    def _show_posts(self, obj):
        posts = obj.posts.all()
        html = ""
        if posts:
            for post in posts:
                html += f'<li><a href="/admin/contents/post/{post.id}/">{post}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
        return self.__NO_POSTS

    _show_posts.short_description = __POSTS
