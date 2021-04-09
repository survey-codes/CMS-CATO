from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableStackedInline, NonSortableParentAdmin
from adminsortable2.admin import SortableInlineAdminMixin
from domain.contents.models import extra, pages, posts, sections
from domain.main.image import get_image_preview
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin
from rangefilter.filter import DateRangeFilter
from presentation import constants as c
from presentation.contents.resources import PostLanguageResource, ImportPostResource, ExportPostResource
from presentation.main.admin import AuditAdmin


PAGE = _('Page')
POSTS = _('Posts')
SECTION_BACKGROUND_COLOR = _("Section' background color")
COUNT_SECTIONS = _('Number of sections')
COUNT_IMAGES = _('Number of images in gallery')
COUNT_TRANSLATIONS = _('Number of translations')
VISIBILITY_HELP_TEXT = _('Check the box if the posts component is visible in this section')
LOGO_PREVIEW = _('Logo(preview)')
EDIT_TEXT = _('Edit in another window')
POST_SETTINGS_PLURAL = _("Posts Settings")
CHOOSE_POSTS = _('Order posts')
SECTION = _('Section')
SECTION_PLURAL = _('Sections')
IMAGE_PREVIEW = _("Preview")
ICON_PREVIEW = _('Icon (Preview)')
GALLERIES = _('Galleries')
NO_POSTS = _("The section has no posts")
NO_PAGES = _("This section is not associated with any page")
NO_SECTIONS = _("This page does not contain sections")
SHOW_PAGES = _('Sections and pages in which appears ')
SHOW_PAGES_SECTION = _('Pages in which appears ')
ONE_GALLERY_ACTIVE = _('Only one banner gallery must be active')
NO_POST_SECTIONS = _("This post is not contained in any section")


#---------INLINES---------
class GeneralDataLanguageInline(admin.StackedInline):
    suit_classes = 'suit-tab suit-tab-language'
    model = extra.GeneralDataLanguage
    extra = 1


class PageLanguageInline(admin.StackedInline):
    model = pages.PageLanguage
    extra = 0
    suit_classes = 'suit-tab suit-tab-language'


class PostLanguageInline(admin.StackedInline):
    model = posts.PostLanguage
    extra = 1
    suit_classes = 'suit-tab suit-tab-language'
    fields = ('language', 'title', 'description')


class PostGalleryInline(SortableStackedInline):
    model = posts.PostGallery
    sortable = 'order'
    extra = 0
    suit_classes = 'suit-tab suit-tab-gallery'
    readonly_fields = ('order', '_preview')
    fields = ('active', 'title', 'image', '_preview', 'is_360', 'youtube_url', 'order')

    def _preview(self, obj):
        image_gallery = obj.image
        if image_gallery:
            return get_image_preview(obj, image_gallery.url, title=IMAGE_PREVIEW)
        return '-'

    _preview.short_description = IMAGE_PREVIEW


class PostSettingsInline(SortableInlineAdminMixin, admin.TabularInline):
    model = posts.PostSettings
    extra = 0
    suit_classes = 'suit-tab suit-tab-post_settings'
    raw_id_fields = ('post',)


class SectionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = sections.SectionSelector
    extra = 0
    readonly_fields = AuditAdmin.readonly_fields
    fields = ('section', 'active',)
    suit_classes = 'suit-tab suit-tab-section'
    raw_id_fields = ('section',)


class SectionLanguageInline(admin.StackedInline):
    model = sections.SectionLanguage
    extra = 1
    suit_classes = 'suit-tab suit-tab-language'


#---------ADMIN---------
@admin.register(extra.GeneralData)
class GeneralDataAdmin(NonSortableParentAdmin):
    inlines = [GeneralDataLanguageInline]
    readonly_fields = ('_logo',) + AuditAdmin.readonly_fields
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'
    list_display = ('id', '_logo')
    fieldsets = (
        ('General', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('logo', '_logo') + AuditAdmin.fieldsets
        }),
    )
    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB)
    )

    def _logo(self, obj):
        image = obj.logo_site
        if image:
            return get_image_preview(obj, img=image.url, title=LOGO_PREVIEW)
        return '-'

    _logo.allow_tags = True
    _logo.short_description = IMAGE_PREVIEW


@admin.register(posts.PostLanguage)
class PostLanguageAdmin(ImportExportModelAdmin):
    resource_class = PostLanguageResource
    readonly_fields = ('language', 'post',)
    fields = ('language', 'title', 'description')

    def has_add_permission(self, request):
        return False


@admin.register(sections.Section)
class SectionAdmin(admin.ModelAdmin):
    actions = ['update_json_content']
    list_display = (
        'title', '_background_preview', '_background_color', 'active', 'creation_date', '_show_pages', '_show_posts'
    )
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'
    inlines = [SectionLanguageInline, PostSettingsInline, ]
    readonly_fields = ('slug', '_background_preview',) + AuditAdmin.readonly_fields
    fieldsets = (
        (SECTION, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('active', 'title', 'background', '_background_preview', 'background_color', 'slug') + AuditAdmin.fieldsets
        }),
        (POST_SETTINGS_PLURAL, {
            'classes': ('wide', 'suit-tab suit-tab-general'),
            'description': VISIBILITY_HELP_TEXT,
            'fields': ('template', 'align')
        }),
    )
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

    def _background_preview(self, obj):
        image = obj.background
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW, )
        return '-'

    _background_preview.allow_tags = True
    _background_preview.short_description = IMAGE_PREVIEW

    def _show_posts(self, obj):
        posts = obj.post_set.all()
        html = ""
        if posts:
            for post in posts:
                html += f'<li><a href="/admin/contents/post/{post.id}/">{post}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
        return NO_POSTS

    _show_posts.short_description = POSTS


@admin.register(pages.Page)
class PageAdmin(DraggableMPTTAdmin, NonSortableParentAdmin):
    DraggableMPTTAdmin.indented_title.short_description = 'Title'
    list_display = ('tree_actions', 'indented_title', 'slug', 'active', 'creation_date', '_show_sections')
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'
    inlines = [SectionInline, PageLanguageInline]
    readonly_fields = ('slug',) + AuditAdmin.readonly_fields
    fieldsets = (
        (PAGE, {
            'classes': ('suit-tab suit-tab-page',),
            'fields': ('active', 'title', 'parent', 'inner_menu', 'slug') + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('page', PAGE),
        ('language', c.LANGUAGE_TAB),
        ('section', SECTION_PLURAL),
    )

    def _show_sections(self, obj):
        sections = obj.sections.all()
        html = ""
        if sections.exists():
            for section in sections:
                html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
        return NO_SECTIONS

    _show_sections.short_description = SECTION_PLURAL

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        return queryset.annotate(section_count=Count('section'))


class CountImages(admin.SimpleListFilter):
    title = COUNT_IMAGES
    parameter_name = '_count_images'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is the coded value for the option that will
        appear in the URL query. The second element is the human-readable name for the option that will appear
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


@admin.register(posts.Post)
class PostAdmin(ImportExportModelAdmin, DraggableMPTTAdmin, NonSortableParentAdmin):
    resource_class = ExportPostResource
    mptt_level_indent = 20
    list_display = (
        'tree_actions',
        'indented_title',
        'active',
        'slug',
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
    readonly_fields = ('_preview', 'slug',) + AuditAdmin.readonly_fields
    fieldsets = (
        ('Post', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('active', 'title', 'logo', '_preview', 'icon', 'parent', 'link', 'slug') + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('general', 'General'),
        ('language', c.LANGUAGE_TAB),
        ('gallery', 'Gallery'),
    )

    def get_import_resource_class(self):
        return ImportPostResource

    def _show_pages(self, obj):
        sections = obj.sections.all()
        html = ""
        if sections.exists():
            for section in sections:
                pages = section.pages.all()
                if pages.exists():
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
        return queryset.annotate(image_count=Count('postgallery'), language_count=Count('translations'))


@admin.register(sections.SectionTemplate)
class SectionTemplateAdmin(admin.ModelAdmin):
    readonly_fields = ('_preview',)
    fieldsets = (
        (None, {
            'fields': (('name', 'nickname'), 'preview', '_preview')
        }),
    )
    list_display = ('name', 'nickname', '_preview')

    def _preview(self, obj):
        image = obj.preview
        if image:
            return get_image_preview(obj, img=image.url, title=IMAGE_PREVIEW)
        return '-'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
