from adminsortable.admin import SortableStackedInline, NonSortableParentAdmin
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin, messages
from django.contrib.admin import register
from django.contrib.admin.options import StackedInline
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.forms import BaseInlineFormSet
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin
from rangefilter.filter import DateRangeFilter

from domain.contents.models import (
    Banner, BannerGallery, BannerLanguage, Contact, ContactLanguage, GallerySelector, GeneralData, GeneralDataLanguage,
    Page, PageLanguage, PartnersGallery, Post, PostGallery, PostLanguage, PostSettings, Section,
    SectionLanguage, SectionSelector, SectionTemplate, SocialNetwork, Tag, TITLE
)
from domain.main.image import get_image_preview
from presentation import constants as c
from presentation.contents.resources import PostLanguageResource, ImportPostResource, ExportPostResource
from presentation.main.admin import AuditAdmin

PAGE = _('Page')
POST = _('Post')
SECTION_BACKGROUND_COLOR = _("Section's background color")
COUNT_SECTIONS = _('Number of sections')
COUNT_IMAGES = _('Number of images in gallery')
COUNT_TRANSLATIONS = _('Number of translations')
VISIBILITY_HELP_TEXT = _('check the box if the posts component is visible in this section')
LOGO_PREVIEW = _('Logo(preview)')
EDIT_TEXT = _('Edit in another window')
BANNER_LANGUAGE_MODIFY = _("Edit banner's fields in language")
GALLERY = _('Gallery')
GALLERY_SELECTOR = _("Select banners galleries")
POST_SETTINGS_PLURAL = _("Posts Settings")
CHOOSE_POSTS = _('Order posts')
SECTION = _('Section')
SECTION_PLURAL = _('Sections')
CONTACT_INFORMATION = _('Contact Information')
BANNER_LANGUAGE_SAVE = _('Save and continue to edit banner language fields')
IMAGE_PREVIEW = _("Preview")
SOCIAL_NETWORK_PLUR = _('Social networks')
ICON_PREVIEW = _('Icon (Preview)')
GALLERIES = _('Galleries')
NO_POSTS = _("The section has no posts")
FIELD_MSG_GALLERY = _(
    "(choose a gallery, click on save and continue editing to see a preview of the first banner of it)")
IMAGE_INSTITUTION = _('Institution image')
PARTNERS_GALLERY = _("Institutional links")
NO_PAGES = _("This section is not associated with any page")
NO_SECTIONS = _("This page does not contain sections")
SHOW_PAGES = _('Sections and pages in which appears ')
SHOW_PAGES_SECTION = _('Pages in which appears ')
ONE_GALLERY_ACTIVE = _('Only one banner gallery must be active')
NO_POST_SECTIONS = _("This post is not contained in any section")


class BannerLanguageInline(admin.StackedInline):
    model = BannerLanguage
    extra = 0
    readonly_fields = ['banner_metadata']
    suit_classes = 'suit-tab suit-tab-language'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    actions = ['update_json_content']
    readonly_fields = ['_preview', 'logo_preview', 'slug_banner']
    inlines = [BannerLanguageInline, ]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                'title',
                'image',
                '_preview',
                'image_360',
                'animated_logo',
                'logo_preview',
                'button_link',
                'icon_css_banner',
                'url_youtube',
                'slug_banner',
            )
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB),
    )

    def logo_preview(self, obj):
        image = obj.animated_logo
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    logo_preview.allow_tags = True
    logo_preview.short_description = IMAGE_PREVIEW

    def _preview(self, obj):
        image = obj.image
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    _preview.allow_tags = True
    _preview.short_description = IMAGE_PREVIEW

    def update_json_content(self, request, queryset):
        from .utils import update_json_content_banner
        for banner in queryset:
            update_json_content_banner(banner)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"


class BannerInline(SortableStackedInline):
    model = Banner
    extra = 0
    suit_classes = 'suit-tab suit-tab-banner'
    readonly_fields = ('banner_language', '_preview', 'logo_preview', 'slug_banner',) + AuditAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (
                'active',
                'title',
                'image',
                '_preview',
                'image_360',
                'animated_logo',
                'logo_preview',
                'button_link',
                'icon_css_banner',
                'url_youtube',
                'banner_language',
                'slug_banner',
            )
        }),
    )

    def banner_language(self, obj=None):
        if obj.pk:
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            text = EDIT_TEXT
            return format_html('<a href="{url}#language" target=' + '_blank' + '>{text}</a>', url=url, text=text)
        return BANNER_LANGUAGE_SAVE

    banner_language.allow_tags = True
    banner_language.short_description = BANNER_LANGUAGE_MODIFY

    def logo_preview(self, obj):
        image = obj.animated_logo
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    logo_preview.allow_tags = True
    logo_preview.short_description = IMAGE_PREVIEW

    def _preview(self, obj):
        image = obj.image
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    _preview.allow_tags = True
    _preview.short_description = IMAGE_PREVIEW


@admin.register(BannerGallery)
class BannerGalleryAdmin(NonSortableParentAdmin):
    list_display = ['_preview', 'title', 'creation_date', 'slug_banner_gallery', 'active']
    list_display_links = ['title', ]
    readonly_fields = ('slug_banner_gallery',) + AuditAdmin.readonly_fields
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'
    inlines = [BannerInline, ]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('active', 'title', 'slug_banner_gallery',) + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('general', 'General'),
        ('banner', 'Banners'),
    )

    def _preview(self, obj):
        banner = obj.banner_set.first()
        if banner:
            if banner.image:
                return get_image_preview(banner, banner.image.url, banner.title, 50)
        return get_image_preview(obj, "/static/no-image.png", 'no image', 50)

    _preview.short_description = IMAGE_PREVIEW


class PostSettingsAdmin(admin.ModelAdmin):
    filter_horizontal = ['post', ]
    fieldsets = (
        (None, {
            'fields': ('post',)
        }),
    )


@admin.register(PostLanguage)
class PostLanguageAdmin(ImportExportModelAdmin):
    resource_class = PostLanguageResource
    readonly_fields = ('language', 'post',)
    filter_horizontal = ('tag',)
    fields = (
        'language',
        'post',
        'title_post',
        'subtitle',
        'long_description',
        'tag',
    )

    def has_add_permission(self, request):
        return False


class PostLanguageInline(admin.StackedInline):
    model = PostLanguage
    extra = 0
    suit_classes = 'suit-tab suit-tab-language'
    filter_horizontal = ['tag', ]
    fields = (
        'language',
        'title_post',
        'subtitle',
        'long_description',
        'tag',
    )


class PostGalleryInline(SortableStackedInline):
    model = PostGallery
    sortable = 'order'
    extra = 0
    suit_classes = 'suit-tab suit-tab-gallery'
    readonly_fields = ['order', '_preview', 'slug_post_gallery', 'update_date']

    fields = [
        'active',
        'title',
        'title_translation',
        'image',
        '_preview',
        'image_360',
        'url_youtube',
        'slug_post_gallery',
        'update_date',
        'order'
    ]

    def _preview(self, obj):
        image_gallery = obj.image
        if image_gallery:
            return get_image_preview(obj, image_gallery.url, title=IMAGE_PREVIEW)
        return '-'

    _preview.short_description = IMAGE_PREVIEW


class SectionLanguageInline(admin.StackedInline):
    model = SectionLanguage
    extra = 0
    suit_classes = 'suit-tab suit-tab-language'


class PostSettingsInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PostSettings
    extra = 0
    suit_classes = 'suit-tab suit-tab-post_settings'
    raw_id_fields = ('post',)
    verbose_name = POST


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    actions = ['update_json_content']
    list_display = (
        'id',
        'title',
        'slug_section',
        '_preview',
        'background_color',
        '_background_color',
        'active',
        'creation_date',
        '_show_pages',
        '_show_posts',
        'title_visibility',
        'subtitle_visibility',
        'logo_visibility',
        'tag_visibility',
        'description_visibility',
        'gallery_visibility',

    )
    list_display_links = ('id', 'title')
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'

    inlines = [SectionLanguageInline, PostSettingsInline, ]
    readonly_fields = ('slug_section', '_preview',) + AuditAdmin.readonly_fields
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                          'active',
                          'title',
                          'background',
                          '_preview',
                          'background_color',
                          'slug_section',
                      ) + AuditAdmin.fieldsets
        }),
        (POST_SETTINGS_PLURAL, {
            'classes': ('wide', 'suit-tab suit-tab-general'),
            'description': VISIBILITY_HELP_TEXT,
            'fields': (
                'template',
                'align',
                'title_visibility',
                'logo_visibility',
                'subtitle_visibility',
                'description_visibility',
                'tag_visibility',
                'gallery_visibility',
                'lines_to_show',
            )
        }),
    )
    radio_fields = {'logo_visibility': admin.HORIZONTAL}

    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB),
        ('post_settings', CHOOSE_POSTS),
    )

    def _background_color(self, obj):
        background = obj.background_color
        if background:
            return mark_safe(f'<div style="background-color:{background}; height:50px; width: 50px"></div>')
        else:
            return '-'

    _background_color.short_description = SECTION_BACKGROUND_COLOR

    def _show_pages(self, obj):
        pages = obj.page.all()
        html = ""
        if pages:
            for page in pages:
                html += f'<li><a href="/admin/contents/page/{page.id}/">{page}</a></li>'
                return mark_safe(f'<ul>{html}</ul>')
        return NO_PAGES

    _show_pages.short_description = SHOW_PAGES_SECTION

    def _preview(self, obj):
        image = obj.background
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW, )
        return '-'

    _preview.allow_tags = True
    _preview.short_description = IMAGE_PREVIEW

    def _show_posts(self, obj):
        posts = obj.post_set.all()
        html = ""
        if posts:
            for post in posts:
                html += f'<li><a href="/admin/contents/post/{post.id}/">{post}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
        return NO_POSTS

    _show_posts.short_description = POST

    def update_json_content(self, request, queryset):
        from .utils import update_json_content_section
        for section in queryset:
            update_json_content_section(section)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"


class ContactLanguageInline(StackedInline):
    model = ContactLanguage
    extra = 0
    readonly_fields = ["contact_metadata"]
    suit_classes = 'suit-tab suit-tab-language'
    fieldsets = (
        (None, {
            'fields': ('language',)
        }),
        (CONTACT_INFORMATION, {
            'fields': (
                'about',
                'title_form',
                'subtitle_form',
                'name_form',
                'mail_form',
                'subject_form',
                'body_form',
                'text_button',
                'contact_metadata',
            )
        }),
    )


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    actions = ['update_json_content']
    readonly_fields = ('slug_contact', '_preview',) + AuditAdmin.readonly_fields
    list_display = ('contact_title', 'active',)
    inlines = [ContactLanguageInline, ]
    change_form_template = 'admin/hide_button_save.html'
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields':
                (
                    'active',
                    'contact_title',
                    'background',
                    '_preview',
                    'slug_contact',
                ) + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB),
    )

    def has_add_permission(self, request):
        if Contact.objects.first():
            return False
        return True

    def _preview(self, obj):
        image = obj.background
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    _preview.allow_tags = True
    _preview.short_description = IMAGE_PREVIEW

    def update_json_content(self, request, queryset):
        from .utils import update_json_content_contact
        for contact in queryset:
            update_json_content_contact(contact)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"


class SectionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SectionSelector
    extra = 0
    readonly_fields = AuditAdmin.readonly_fields
    fields = ('section', 'active',)
    suit_classes = 'suit-tab suit-tab-section'
    raw_id_fields = ['section', ]
    verbose_name = SECTION


class GallerySelectorInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(GallerySelectorInlineFormSet, self).clean()
        count = 0
        for form in self.forms:
            if form.cleaned_data['active']:
                count += 1
                if count > 1:
                    form.add_error("active", ValidationError(ONE_GALLERY_ACTIVE))


class GallerySelectorInline(admin.TabularInline):
    model = GallerySelector
    suit_classes = 'suit-tab suit-tab-gallery_selector'
    raw_id_fields = ['banner_gallery', ]
    readonly_fields = ('_preview', 'id')
    fields = ['banner_gallery', '_preview', 'active', ]
    formset = GallerySelectorInlineFormSet
    extra = 0

    def _preview(self, obj):
        has_gallery = obj.banner_gallery
        if has_gallery:
            banner = has_gallery.banner_set.first()
            if banner:
                if banner.image:
                    return get_image_preview(banner, banner.image.url, banner.title, 50)

        return get_image_preview(obj, "/static/no-image.png", 'no image', 50, FIELD_MSG_GALLERY)

    _preview.short_description = IMAGE_PREVIEW


class PageLanguageInline(admin.StackedInline):
    model = PageLanguage
    extra = 0
    suit_classes = 'suit-tab suit-tab-language'


@admin.register(Page)
class PageAdmin(DraggableMPTTAdmin, NonSortableParentAdmin):
    actions = ['update_json_content']
    DraggableMPTTAdmin.indented_title.short_description = TITLE
    list_display = (
        'tree_actions',
        'indented_title',
        'slug_page',
        'active',
        'creation_date',
        '_show_sections',
        '_count_sections',
        '_preview_gallery',
    )
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'
    inlines = [SectionInline, GallerySelectorInline, PageLanguageInline]
    readonly_fields = ('slug_page',) + AuditAdmin.readonly_fields
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-page',),
            'fields': ('page_type', 'active', 'title', 'parent', 'inner_menu', 'slug_page',) + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('page', PAGE),
        ('language', c.LANGUAGE_TAB),
        ('section', SECTION_PLURAL),
        ('gallery_selector', GALLERY_SELECTOR),
    )

    def _preview_gallery(self, obj):

        has_gallery = obj.galleryselector_set.order_by('-active').select_related(
            'banner_gallery').only('banner_gallery').first()
        if has_gallery:
            banner_gallery = has_gallery.banner_gallery
            if banner_gallery:
                banner = banner_gallery.banner_set.first()
                if banner:
                    if banner.image:
                        return get_image_preview(banner, banner.image.url, banner.title, 50)

        return get_image_preview(obj, "/static/no-image.png", 'no image', 50)

    _preview_gallery.short_description = GALLERIES

    def _show_sections(self, obj):
        sections = obj.section_set.all()
        html = ""
        if sections:
            for section in sections:
                html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')

        return NO_SECTIONS

    _show_sections.short_description = SECTION_PLURAL

    def _count_sections(self, obj):
        section_count = obj.section_count
        return section_count

    _count_sections.short_description = COUNT_SECTIONS
    _count_sections.admin_order_field = 'section_count'

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        return queryset.annotate(section_count=Count('section'))

    def update_json_content(self, request, queryset):
        from .utils import update_json_content_page
        for page in queryset:
            update_json_content_page(page)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"


class CountImages(admin.SimpleListFilter):
    title = COUNT_IMAGES

    parameter_name = '_count_images'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ("0", "0"),
            ("1", "1"),
            ("2", "2 - 5"),
            ("3", "6 - 10"),
            ("4", "10+"),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(image_count=0)
        if self.value() == '1':
            return queryset.filter(image_count=1)
        if self.value() == '2':
            return queryset.filter(image_count__gte=2, image_count__lte=5)
        if self.value() == '3':
            return queryset.filter(image_count__gte=6, image_count__lte=10)
        if self.value() == '2':
            return queryset.filter(image_count__gte=10)


@register(Post)
class PostAdmin(ImportExportModelAdmin, DraggableMPTTAdmin, NonSortableParentAdmin):
    actions = ['update_json_content']
    resource_class = ExportPostResource
    mptt_level_indent = 20
    list_display = (
        'tree_actions',
        'indented_title',
        'active',
        'slug_post',
        'creation_date',
        '_count_images',
        '_count_languages',
        '_show_pages'
    )
    search_fields = ('image_count', 'language_count')
    list_filter = (('creation_date', DateRangeFilter), CountImages)
    suit_list_filter_horizontal = ('creation_date', '_count_images',)
    change_list_template = 'admin/change_import_export_filter.html'
    inlines = [PostLanguageInline, PostGalleryInline]
    readonly_fields = ('_preview', 'slug_post',) + AuditAdmin.readonly_fields
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                          'active',
                          'title_post',
                          'logo',
                          '_preview',
                          'icon',
                          'parent',
                          'external_url',
                          'slug_post'
                      ) + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB),
        ('gallery', GALLERY),
    )

    def get_import_resource_class(self):
        return ImportPostResource

    def _show_pages(self, obj):
        sections = obj.section.all()
        html = ""
        if sections:
            for section in sections:
                pages = section.page.all()
                if pages:
                    for page in pages:
                        html += f"<li><a href='/admin/contents/section/{section.id}/'>{section}</a>" \
                                f" | <a href='/admin/contents/page/{page.id}/'>{page}</a></li> "
                else:
                    html += f"<li><a href='/admin/contents/section/{section.id}/'>{section}</a> | {NO_PAGES} </li>"
            return mark_safe(f'<ul>{html}</ul>')
        return NO_POST_SECTIONS

    _show_pages.short_description = SHOW_PAGES

    def _preview(self, obj):
        image = obj.logo
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    _preview.allow_tags = True
    _preview.short_description = IMAGE_PREVIEW

    def _count_languages(self, obj):
        language_count = obj.language_count
        return language_count

    _count_languages.short_description = COUNT_TRANSLATIONS
    _count_languages.admin_order_field = 'language_count'

    def _count_images(self, obj):
        image_count = obj.image_count
        return image_count

    _count_images.short_description = COUNT_IMAGES
    _count_images.admin_order_field = 'image_count'

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        return queryset.annotate(image_count=Count('postgallery'), language_count=Count('postlanguage_post_lang_set'))

    def update_json_content(self, request, queryset):
        from .utils import update_json_content_post
        for post in queryset:
            update_json_content_post(post)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    readonly_fields = ('slug_tag',)
    list_display_links = ('id', 'name',)
    list_display = list_display_links + ('slug_tag',)
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'slug_tag')
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
    )


@register(SectionTemplate)
class SectionTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', '_preview')

    def _preview(self, obj):
        image = obj.preview
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    def has_add_permission(self, request):
        return False


class SocialNetworkInline(SortableStackedInline):
    model = SocialNetwork
    extra = 0
    suit_classes = 'suit-tab suit-tab-social_networks'
    readonly_fields = ('get_icon', 'slug',)
    fields = ('active', 'name', 'icon', 'get_icon', 'url', 'icon_css', 'slug')
    list_display = ('name', 'get_icon')

    def get_icon(self, obj):
        image = obj.icon
        if image:
            return get_image_preview(obj, img=image.url, title='')
        return '-'

    get_icon.allow_tags = True
    get_icon.short_description = ICON_PREVIEW


class GeneralDataLanguageInline(admin.StackedInline):
    suit_classes = 'suit-tab suit-tab-language'
    model = GeneralDataLanguage
    extra = 0


class PartnersGalleryInline(SortableStackedInline):
    model = PartnersGallery
    extra = 0
    fields = ['image', '_partner_preview', 'url', 'active', ]
    readonly_fields = ['_partner_preview', ]
    suit_classes = 'suit-tab suit-tab-partner_links'

    def _partner_preview(self, obj):
        image = obj.image
        if image:
            return get_image_preview(obj, img=image.url, title=LOGO_PREVIEW)
        return '-'

    _partner_preview.allow_tags = True
    _partner_preview.short_description = f'{IMAGE_INSTITUTION} ({IMAGE_PREVIEW})'


@admin.register(GeneralData)
class GeneralAdmin(NonSortableParentAdmin):
    actions = ['update_json_content']
    inlines = [SocialNetworkInline, GeneralDataLanguageInline, PartnersGalleryInline]
    readonly_fields = ('_logo', 'slug_general_data') + AuditAdmin.readonly_fields
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'

    list_display = ('title_one', 'active', '_logo')
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                          'active',
                          'logo_site',
                          '_logo',
                          'title_one',
                          'slug_general_data',
                      ) + AuditAdmin.fieldsets
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB),
        ('social_networks', SOCIAL_NETWORK_PLUR),
        ('partner_links', PARTNERS_GALLERY)
    )

    def _logo(self, obj):
        image = obj.logo_site
        if image:
            return get_image_preview(obj, img=image.url, title=LOGO_PREVIEW)
        return '-'

    _logo.allow_tags = True
    _logo.short_description = IMAGE_PREVIEW

    def update_json_content(self, request, queryset):
        from .utils import update_json_content_general_data
        for general_data in queryset:
            update_json_content_general_data((general_data))

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"
