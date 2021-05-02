# Updated by nigga 2021-03-14 14:17
from adminsortable.admin import SortableStackedInline, NonSortableParentAdmin
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin
from rangefilter.filter import DateRangeFilter

from cms.infrastructure.data_access.entities.contents.models import posts, sections
from cms.infrastructure.data_access.entities.main.image import get_image_preview
from cms.presentation import constants as c
from cms.presentation.constants import NO_PAGES, IMAGE_PREVIEW
from cms.presentation.contents.resources import PostLanguageResource, ImportPostResource, ExportPostResource
from cms.presentation.main.admin.admin import Audit2Admin

COUNT_SECTIONS = _('Number of sections')
COUNT_IMAGES = _('Number of images in gallery')
COUNT_TRANSLATIONS = _('Number of translations')

LOGO_PREVIEW = _('Logo')
EDIT_TEXT = _('Edit in another window')

ICON_PREVIEW = _('Icon')
GALLERIES = _('Galleries')

SHOW_PAGES = _('Sections and pages in which appears ')

NO_POST_SECTIONS = _("This post is not contained in any section")


# ---------INLINES---------
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
    readonly_fields = Audit2Admin.readonly_fields
    fields = ('section', 'active',)
    suit_classes = 'suit-tab suit-tab-section'
    raw_id_fields = ('section',)


# ---------ADMIN---------


@admin.register(posts.PostLanguage)
class PostLanguageAdmin(ImportExportModelAdmin):
    resource_class = PostLanguageResource
    readonly_fields = ('language', 'post',)
    fields = ('language', 'title', 'description')

    def has_add_permission(self, request):
        return False


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
    readonly_fields = ('_preview', 'slug',) + Audit2Admin.readonly_fields
    fieldsets = (
        ('Post', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('active', 'title', 'logo', '_preview', 'icon', 'parent', 'link', 'slug') + Audit2Admin.fieldsets
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
