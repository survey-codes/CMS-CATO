from adminsortable.models import SortableMixin
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from url_or_relative_url_field.fields import URLOrRelativeURLField

from domain.constants import (
    SLUG, RELATED_NAME, JSON_CONTENT, ACTIVE, MAX_LENGTH_50, MENU, LANGUAGE_TAB, LANGUAGE_APP_PLURAL, MAX_LENGTH_200
)
from domain.entities.main.models import Audit, LanguageAbstract, CREATION_DATE_KEY
from domain.entities.menus.models import Menu

APP_LABEL = "contents"

MAX_LENGTH_20 = 20
MAX_LENGTH_NAME = 35
MAX_LENGTH_SHORT_TITLE = 100
MAX_LENGTH_DESCRIPTION = 500
ORDER_VALUE_DEFAULT = 0
MAX_LENGTH_URL_YOUTUBE = 255
BANNERS_TITLE = _("Banner's title")
BACKGROUND_IMAGE = _('Background image')
PATH_APP = 'Contents'
PATH_BANNER = f'{PATH_APP}/banners/'
PATH_ANIMATED_LOGO = f'{PATH_BANNER}/animated_logos'
PATH_ICON_POST = f'{PATH_BANNER}/icon_post'
IMAGE_360 = _("is it a 360 image?")
IMAGE_HELP_TEXT = _('Check the box if is a 360 image')
LOGO_ANIMATE = _('animated logo')
BANNER_LINK = _('Add link to banner')
ICON_CSS_BUTTON_BANNER = _('icon css button banner')
ICON_LIST = _('List of icons')
ICON_LIST_URL = 'https://fontawesome.com/v4.7.0/icons/'
HELP_TEXT_ICON_CSS_BANNER = f"{ICON_LIST}: <a href={ICON_LIST_URL} target={'_blank'}> {ICON_LIST_URL} </a>"
YOUTUBE_VIDEO = _("Youtube video url")
BANNER_GALLERY = _("Banners gallery")
BANNER = _('Banner')
BANNER_PLURAL = _('Banners')
N_N = "N/N"
BANNERS_SUBTITLE = _("Banner's subtitle")
BANNERS_DESCRIPTION = _("Banner's description text")
BUTTON_BANNER = _('text button banner')
BANNER_LANG_KEY = "banner_lang"
FIELD_BANNER_LANGUAGE = _("Banner's language")
BANNER_LANGUAGE_PLURAL = _("Banner's laguages")
BANNER_GALLERY_TITLE = _("Banner's gallery title")
DEFAULT_VALUE = "-"
BANNER_GALLERY_PLURAL = _("Banners galleries")
PAGE_FK_BANNER_GALLERY = _('Show banner gallery in this page')
GALLERY_SELECTOR = _("Select banners galleries")
GALLERY_ERROR = _('Please select galleries that are active')
EMPTY_FIELD = _("This field can't be empty")
GALLERY_MESSAGE_UNIQUE = _("The same gallery shouldn't be added more than once")
PAGE_TYPE = _("Page's type")
MAKING_KEY = "MAKING"
CONTENT_KEY = "CONTENT"
PAGE_TYPE_CHOICES = (
    (MAKING_KEY, _('Construcción')),
    (CONTENT_KEY, _('Contenido'))
)
TITLE = _('Title')
PAGE_PARENT = _("Page's parent")
PAGE = _('Page')
PAGE_LANG_KEY = 'page_lang'
POST_LANG_KEY = 'post_lang'
SECTION_LANG_KEY = 'section_lang'
CONTACT_LANG_KEY = "contact_lang"
GENERAL_DATA_LANG_KEY = "general_data_lang"
PAGE_TITLE = _("Page's title")
PAGE_DESCRIPTION = _("Page's description")
EMPTY_STRING = ""
PAGE_LANGUAGE = _('Page language')
PAGE_LANGUAGE_PLURAL = _('Page languages')
POST_TITLE = _("Post's title")
LOGO_POST = _("Post's image")
ICON_POST = _("Post's icon")
POST_PARENT = _("Post's parent")
EXTERNAL_URL = _("External URL")
SECTION_PLURAL = _('Sections')
POST_SUBTITLE = _("Post's subtitle")
POST_DESCRIPTION = _("Post's description text")
POST = _('Post')
TAG = _('Tags')
POST_LANGUAGE = _('Post language')
POST_LANGUAGE_PLURAL = _('Post languages')
PAGE_SECTION = _("Page's section")
SECTION = _('Section')
SELECT_SECTION = _('Select section')
SELECT_SECTIONS = _('Select sections')
SECTION_TITLE = _("Section's title")
PATH_SECTION_BACKGROUND = f'{PATH_APP}/sections/background'
SECTION_BACKGROUND_COLOR = _("Section's background color")
DEFAULT_COLOR = "#FFFFFF"
ALIGN_TEXTS = _("Posts texts alignment")
ALIGN_CHOICES = (
    ('RIGHT', _('Right')),
    ('LEFT', _('Left')),
    ('RIGHT_LEFT', _('Right - left')),
    ('LEFT_RIGHT', _('left - right'))
)
DEFAULT_ALIGN = "RIGHT"
COMPONENT_TYPE = _("Section template")
LINES_VB = _("Display this many lines before show more")
QUANTITY_LINES = _("Between one and four lines")
TITLE_AS = _('Title visibility')
SUBTITLE = _('Subtitle visibility')
LOGO_VISIBILITY = _('Image visibility')
LOGO_IN = (
    (1, _('Above title')),
    (2, _('To the left of the title')),
    (3, _('To the left of the post')),
    (4, _('as background')),
    (5, _('No visible'))
)
TAGS_VISIBILITY = _('Tags visibility')
DESCRIPTION = _('Description visibility')
GALLERY_VISIBILITY = _('Gallery visibility')
LOGO_VISIBILITY_ERROR = _('You have to show the title to allocate the logo to the left of it')
RESTRICTION = _("Make sure this value is less or equal than 4 and greater or equal than 1")
SECTION_DESCRIPTION = _("Section's description")
SECTION_LANGUAGE_SINGULAR = _("Section's language")
SECTION_LANGUAGE_PLURAL = _("Section's languages")
TAG_NAME = _('Tag name')
TAG_SINGULAR = _('Tag')
SECTION_POST = _("Section's posts")
SHOW_FAMILY = _('Show family')
SHOW_FAMILY_HELP = _("Check the box if you want the post's family to shown in the section")
POST_SETTINGS = _('Post settings')
CHOOSE_POSTS = _('Order posts')
IMAGE_NAME = _("Image name in spanish")
IMAGE_NAME_TRANSLATION = _("Image name in english")
LOAD_IMAGE = _('Load image')
PATH_IMAGES_GALLERIES = f'{PATH_APP}/Post_gallery_images'
POST_GALLERY = _("Image")
POST_GALLERY_PLURAL = _('Images')
POST_GALLERY_ERROR = _("You can't save an image and youtube video into the same gallery")
TEMPLATE_NAME = _('Template name')
TEMPLATE_NICKNAME = _('Template nickname')
TEMPLATE_TYPE_PLURAL = _("Section templates")
CONTACT_TITLE = _('Contact title')
CONTACT = _('Contact')
BACKGROUND_FORM_IMAGE = _('Background form image')
PATH_CONTACT_BACKGROUND = f'{PATH_APP}/contacts/background'
CONTACT_PLURAL = _('Contacts')
CONTACT_ABOUT = _('Contact description')
TITLE_FORM_CONTACT = _('Title form contact')
SUBTITLE_FORM_CONTACT = _('Subtitle form contact')
NAME_FORM_CONTACT = _('Name form contact')
MAIL_FORM_CONTACT = _('Mail form contact')
AFFAIR_FORM_CONTACT = _('Affair form contact')
BODY_FORM_CONTACT = _('Body form contact')
TEXT_BUTTON_FORM_CONTACT = _('Text button form contact')
SOCIAL_NAME = _('Social network name')
ICON = _('Icon')
PATH_APP_TOOLS = 'Tools'
PATH_LOGO_SOCIAL = f'{PATH_APP_TOOLS}/Logo_social'
ICON_CSS = _('Icon css')
LINK_SOCIAL = _('link social')
ORDER = _('order')
FOOTER = _('Footer')
SOCIAL_NETWORK_SING = _('Social network')
SOCIAL_NETWORK_PLUR = _('Social networks')
LOGO = _('Logo')
PATH_LOGO_SITE = f'{PATH_APP_TOOLS}/logos'
GENERAL_DATA = _("General data")
ONE_GDATA_ACTIVE = _('Only one general data can be active')
IMAGE_INSTITUTION = _('Institution image')
PATH_PARTNERS = f'{PATH_APP}/partner_images'
URL_INSTITUTION = _("Institution url")
PARTNERS_GALLERY = _("Institutional links")
STR_PARTNER = _('partners link number ')
FOOTER_ONE = _('footer title one')
FOOTER_ABOUT = _('Footer description')
FOOTER_TWO = _('footer title two')
GENERAL_DATA_LANGUAGE = _("General data language")
GENERAL_DATA_LANGUAGE_PLURAL = _("General data languages")


class Banner(SortableMixin, Audit):
    title = models.CharField(
        verbose_name=BANNERS_TITLE,
        max_length=MAX_LENGTH_200
    )

    image = models.ImageField(
        verbose_name=BACKGROUND_IMAGE,
        upload_to=PATH_BANNER,
        null=True,
        blank=True
    )

    image_360 = models.BooleanField(
        verbose_name=IMAGE_360,
        help_text=IMAGE_HELP_TEXT,
        default=False,
        blank=True
    )

    animated_logo = models.ImageField(
        verbose_name=LOGO_ANIMATE,
        upload_to=PATH_ANIMATED_LOGO,
        null=True,
        blank=True
    )

    button_link = URLOrRelativeURLField(
        verbose_name=BANNER_LINK,
        blank=True,
        null=True,
        default=None
    )

    icon_css_banner = models.CharField(
        verbose_name=ICON_CSS_BUTTON_BANNER,
        max_length=MAX_LENGTH_20,
        blank=True,
        null=True,
        default=None,
        help_text=HELP_TEXT_ICON_CSS_BANNER
    )

    order = models.PositiveSmallIntegerField(
        default=ORDER_VALUE_DEFAULT
    )

    url_youtube = models.CharField(
        verbose_name=YOUTUBE_VIDEO,
        max_length=MAX_LENGTH_URL_YOUTUBE,
        blank=True,
        null=True
    )

    banner_gallery = models.ForeignKey(
        'BannerGallery',
        verbose_name=BANNER_GALLERY,
        on_delete=models.CASCADE,
        null=True,
    )

    slug_banner = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = BANNER
        verbose_name_plural = BANNER_PLURAL
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_banner = slugify(self.title)
        super(Banner, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title or N_N}"


class BannerLanguage(LanguageAbstract):
    title = models.CharField(
        verbose_name=BANNERS_TITLE,
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True
    )

    subtitle = models.CharField(
        verbose_name=BANNERS_SUBTITLE,
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True
    )

    banner_description = RichTextField(
        verbose_name=BANNERS_DESCRIPTION,
        blank=True,
        null=True
    )

    button_text = models.CharField(
        verbose_name=BUTTON_BANNER,
        max_length=MAX_LENGTH_20,
        blank=True,
        null=True,
        default=None
    )

    banner = models.ForeignKey(
        'Banner',
        verbose_name=BANNER,
        on_delete=models.CASCADE,
        related_name=RELATED_NAME.format(BANNER_LANG_KEY)
    )

    banner_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder
    )

    class Meta:
        unique_together = (('language', 'banner'),)
        verbose_name = FIELD_BANNER_LANGUAGE
        verbose_name_plural = BANNER_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.language)


class BannerGallery(Audit):
    title = models.CharField(
        verbose_name=BANNER_GALLERY_TITLE,
        max_length=MAX_LENGTH_200,
        null=False,
        default=BANNER_GALLERY
    )

    slug_banner_gallery = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    def save(self, *args, **kwargs):
        self.slug_banner_gallery = slugify(self.title)
        super(BannerGallery, self).save(*args, **kwargs)

    class Meta:
        ordering = [f'-{CREATION_DATE_KEY}']
        verbose_name = BANNER_GALLERY
        verbose_name_plural = BANNER_GALLERY_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.title)


class GallerySelector(models.Model):
    active = models.BooleanField(
        verbose_name=ACTIVE,
        default=False
    )

    page = models.ForeignKey(
        'Page',
        verbose_name=PAGE_FK_BANNER_GALLERY,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    banner_gallery = models.ForeignKey(
        BannerGallery,
        verbose_name=GALLERY_SELECTOR,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def clean(self):
        # super(__class__, self).clean()
        gallery = self.banner_gallery
        if gallery:
            if not gallery.active:
                raise ValidationError({
                    "banner_gallery": GALLERY_ERROR
                })
        else:
            raise ValidationError({
                "banner_gallery": EMPTY_FIELD,
            })

    class Meta:
        ordering = ['-active', ]
        unique_together = (('page', 'banner_gallery'),)
        verbose_name = BANNER_GALLERY
        verbose_name_plural = BANNER_GALLERY_PLURAL
        app_label = APP_LABEL

    def unique_error_message(self, model_class, unique_check):
        return GALLERY_MESSAGE_UNIQUE

    def __str__(self):
        return f"{self.page.title} gallery {self.id}"


class Page(MPTTModel, Audit):
    page_type = models.CharField(
        verbose_name=PAGE_TYPE,
        max_length=MAX_LENGTH_20,
        null=False,
        blank=False,
        choices=PAGE_TYPE_CHOICES,
        default=MAKING_KEY
    )

    title = models.CharField(
        verbose_name=TITLE,
        max_length=MAX_LENGTH_50,
        null=False,
        blank=False,
        unique=True
    )

    parent = TreeForeignKey(
        'self',
        verbose_name=PAGE_PARENT,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    inner_menu = models.ForeignKey(
        Menu,
        verbose_name=MENU,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    gallery_selector = models.ManyToManyField(
        'BannerGallery',
        verbose_name=GALLERY_SELECTOR,
        through='GallerySelector',
        blank=True,
    )

    order = models.PositiveSmallIntegerField(
        default=0,
    )

    slug_page = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    class Meta:
        verbose_name = PAGE
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_page = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class PageLanguage(LanguageAbstract):
    title = models.CharField(
        verbose_name=PAGE_TITLE,
        max_length=MAX_LENGTH_50
    )

    description = RichTextField(
        verbose_name=PAGE_DESCRIPTION,
        blank=True,
        null=True,
        default=EMPTY_STRING
    )

    page = models.ForeignKey(
        Page,
        verbose_name=PAGE,
        on_delete=models.CASCADE,
        related_name=RELATED_NAME.format(PAGE_LANG_KEY)
    )

    page_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'page'),)
        verbose_name = PAGE_LANGUAGE
        verbose_name_plural = PAGE_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.language)


class Post(MPTTModel, Audit):
    title_post = models.CharField(
        verbose_name=POST_TITLE,
        max_length=MAX_LENGTH_50,
        blank=False,
        null=False
    )

    logo = models.ImageField(
        verbose_name=LOGO_POST,
        upload_to=PATH_ANIMATED_LOGO,
        blank=True
    )

    icon = models.ImageField(
        verbose_name=ICON_POST,
        upload_to=PATH_ICON_POST,
        blank=True
    )

    parent = TreeForeignKey(
        'self',
        verbose_name=POST_PARENT,
        null=True,
        on_delete=models.CASCADE,
        blank=True
    )

    external_url = models.URLField(
        verbose_name=EXTERNAL_URL,
        null=True,
        blank=True
    )

    slug_post = models.SlugField(
        default=DEFAULT_VALUE
    )

    section = models.ManyToManyField(
        'Section',
        verbose_name=SECTION_PLURAL,
        through='PostSettings'
    )

    class Meta:
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_post = slugify(self.title_post)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title_post)


class PostLanguage(LanguageAbstract):
    title_post = models.CharField(
        verbose_name=POST_TITLE,
        max_length=MAX_LENGTH_50,
        blank=True,
        null=True
    )

    subtitle = models.CharField(
        verbose_name=POST_SUBTITLE,
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True
    )

    long_description = RichTextField(
        verbose_name=POST_DESCRIPTION,
        blank=True,
        null=True
    )

    post = models.ForeignKey(
        Post,
        verbose_name=POST,
        on_delete=models.CASCADE,
        related_name=RELATED_NAME.format(POST_LANG_KEY)
    )

    tag = models.ManyToManyField(
        'Tag',
        verbose_name=TAG,
        blank=True
    )

    post_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'post'),)
        ordering = ['post', ]
        verbose_name = POST_LANGUAGE
        verbose_name_plural = POST_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.post.title_post} - {self.language}'


class SectionSelector(Audit):
    page = models.ForeignKey(
        'Page',
        verbose_name=PAGE_SECTION,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    section = models.ForeignKey(
        'Section',
        verbose_name=SECTION,
        on_delete=models.SET_NULL,
        null=True
    )

    order = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = SELECT_SECTION
        verbose_name_plural = SELECT_SECTIONS
        app_label = APP_LABEL

    def __str__(self):
        return f"{self.section}"


class Section(Audit):
    title = models.CharField(
        verbose_name=SECTION_TITLE,
        max_length=MAX_LENGTH_SHORT_TITLE,
        unique=True
    )

    page = models.ManyToManyField(
        'Page',
        verbose_name=PAGE_SECTION,
        blank=True,
        through='SectionSelector'
    )

    background = models.ImageField(
        verbose_name=BACKGROUND_IMAGE,
        upload_to=PATH_SECTION_BACKGROUND,
        blank=True,
        null=True
    )

    background_color = ColorField(
        verbose_name=SECTION_BACKGROUND_COLOR,
        default=DEFAULT_COLOR
    )

    align = models.CharField(
        verbose_name=ALIGN_TEXTS,
        max_length=MAX_LENGTH_20,
        choices=ALIGN_CHOICES,
        default=DEFAULT_ALIGN
    )

    template = models.ForeignKey(
        'SectionTemplate',
        verbose_name=COMPONENT_TYPE,
        null=True,
        on_delete=models.CASCADE
    )

    slug_section = models.SlugField(
        default=DEFAULT_VALUE,
        verbose_name=SLUG
    )

    order = models.PositiveSmallIntegerField(
        default=0
    )

    lines_to_show = models.SmallIntegerField(
        default=1,
        verbose_name=LINES_VB,
        help_text=QUANTITY_LINES
    )

    '''---------------------Visibility---------------------'''
    title_visibility = models.BooleanField(
        verbose_name=TITLE_AS,
        default=True
    )

    subtitle_visibility = models.BooleanField(
        verbose_name=SUBTITLE,
        default=False
    )

    logo_visibility = models.PositiveSmallIntegerField(
        verbose_name=LOGO_VISIBILITY,
        choices=LOGO_IN,
        default=3,
        blank=False,
        null=False
    )

    tag_visibility = models.BooleanField(
        verbose_name=TAGS_VISIBILITY,
        default=False
    )

    description_visibility = models.BooleanField(
        verbose_name=DESCRIPTION,
        default=False
    )

    gallery_visibility = models.BooleanField(
        verbose_name=GALLERY_VISIBILITY,
        default=False
    )
    '''----------------------------------------------------'''

    class Meta:
        ordering = ['order', ]
        verbose_name = SECTION
        verbose_name_plural = SECTION_PLURAL
        app_label = APP_LABEL

    def clean(self):
        if self.logo_visibility == 2 and self.title_visibility is False:
            raise ValidationError({
                "title_visibility": LOGO_VISIBILITY_ERROR

            })
        if self.lines_to_show > 4 or self.lines_to_show < 1:
            raise ValidationError({
                "lines_to_show": RESTRICTION
            })

    def save(self, *args, **kwargs):
        self.slug_section = slugify(self.title)
        super(Section, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class SectionLanguage(LanguageAbstract):
    title = models.CharField(
        verbose_name=SECTION_TITLE,
        max_length=MAX_LENGTH_SHORT_TITLE,
        blank=True,
        null=True
    )

    description = models.CharField(
        verbose_name=SECTION_DESCRIPTION,
        max_length=MAX_LENGTH_DESCRIPTION,
        null=True,
        blank=True
    )

    section = models.ForeignKey(
        Section,
        verbose_name=SECTION,
        on_delete=models.CASCADE,
        related_name=RELATED_NAME.format(SECTION_LANG_KEY)
    )

    sect_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'section'),)
        verbose_name = SECTION_LANGUAGE_SINGULAR
        verbose_name_plural = SECTION_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.language)


class Tag(models.Model):
    name = models.CharField(
        verbose_name=TAG_NAME,
        max_length=MAX_LENGTH_50
    )

    slug_tag = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    class Meta:
        verbose_name = TAG_SINGULAR
        verbose_name_plural = TAG
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_tag = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return f'#{self.name}'


class PostSettings(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name=SECTION_POST,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    section = models.ForeignKey(
        'Section',
        verbose_name=SECTION,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    show_family = models.BooleanField(
        verbose_name=SHOW_FAMILY,
        default=False,
        help_text=SHOW_FAMILY_HELP
    )

    order = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = POST_SETTINGS
        verbose_name_plural = CHOOSE_POSTS
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.section}'


class PostGallery(SortableMixin, Audit):
    active = models.BooleanField(
        verbose_name=ACTIVE,
        default=True
    )

    title = models.CharField(
        verbose_name=IMAGE_NAME,
        max_length=MAX_LENGTH_SHORT_TITLE,
        null=True
    )

    title_translation = models.CharField(
        verbose_name=IMAGE_NAME_TRANSLATION,
        max_length=MAX_LENGTH_SHORT_TITLE,
        null=True
    )

    image = models.ImageField(
        verbose_name=LOAD_IMAGE,
        upload_to=PATH_IMAGES_GALLERIES,
        null=True,
        blank=True
    )

    image_360 = models.BooleanField(
        verbose_name=IMAGE_360,
        help_text=IMAGE_HELP_TEXT,
        default=False,
        blank=True
    )

    url_youtube = models.CharField(
        verbose_name=YOUTUBE_VIDEO,
        max_length=MAX_LENGTH_URL_YOUTUBE,
        blank=True,
        null=True
    )

    post = models.ForeignKey(
        Post,
        verbose_name=POST,
        on_delete=models.CASCADE
    )

    order = models.SmallIntegerField(
        default=0
    )

    slug_post_gallery = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = POST_GALLERY
        verbose_name_plural = POST_GALLERY_PLURAL
        app_label = APP_LABEL

    def clean(self):
        if self.image and self.url_youtube:
            raise ValidationError(
                {
                    "image": POST_GALLERY_ERROR,
                }
            )
        pass

    def save(self, *args, **kwargs):
        self.slug_post_gallery = slugify(self.title)
        super(PostGallery, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.post}'


class SectionTemplate(models.Model):
    name = models.CharField(
        verbose_name=TEMPLATE_NAME,
        max_length=MAX_LENGTH_NAME
    )

    nickname = models.CharField(
        verbose_name=TEMPLATE_NICKNAME,
        max_length=MAX_LENGTH_NAME,
        null=True,
        blank=True
    )

    preview = models.ImageField(
        verbose_name=LOAD_IMAGE,
        upload_to=PATH_IMAGES_GALLERIES,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = TEMPLATE_NAME
        verbose_name_plural = TEMPLATE_TYPE_PLURAL
        unique_together = (('name', 'nickname'),)
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.name}'


class Contact(Audit):
    contact_title = models.CharField(
        verbose_name=CONTACT_TITLE,
        max_length=MAX_LENGTH_SHORT_TITLE,
        null=True,
        default=CONTACT
    )

    background = models.ImageField(
        verbose_name=BACKGROUND_FORM_IMAGE,
        upload_to=PATH_CONTACT_BACKGROUND,
        blank=True,
        null=True
    )

    slug_contact = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    class Meta:
        verbose_name = CONTACT
        verbose_name_plural = CONTACT_PLURAL
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_contact = slugify(self.contact_title)
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.contact_title}'


class ContactLanguage(LanguageAbstract):
    about = RichTextField(
        verbose_name=CONTACT_ABOUT,
        blank=True,
        null=True,
        default=EMPTY_STRING
    )

    contact = models.ForeignKey(
        Contact,
        verbose_name=CONTACT,
        related_name=RELATED_NAME.format(CONTACT_LANG_KEY),
        on_delete=models.CASCADE,
    )

    title_form = models.CharField(
        verbose_name=TITLE_FORM_CONTACT,
        max_length=MAX_LENGTH_50,
        default=EMPTY_STRING
    )

    subtitle_form = models.CharField(
        verbose_name=SUBTITLE_FORM_CONTACT,
        max_length=MAX_LENGTH_50,
        default=EMPTY_STRING
    )

    name_form = models.CharField(
        verbose_name=NAME_FORM_CONTACT,
        max_length=MAX_LENGTH_50,
        default=EMPTY_STRING
    )

    mail_form = models.CharField(
        verbose_name=MAIL_FORM_CONTACT,
        max_length=MAX_LENGTH_50,
        default=EMPTY_STRING
    )

    subject_form = models.CharField(
        verbose_name=AFFAIR_FORM_CONTACT,
        max_length=MAX_LENGTH_50,
        default=EMPTY_STRING
    )

    body_form = models.TextField(
        verbose_name=BODY_FORM_CONTACT,
        default=EMPTY_STRING
    )

    text_button = models.CharField(
        verbose_name=TEXT_BUTTON_FORM_CONTACT,
        max_length=MAX_LENGTH_50,
        default=EMPTY_STRING
    )

    contact_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder
    )

    class Meta:
        unique_together = (('language', 'contact'),)
        verbose_name = LANGUAGE_TAB
        verbose_name_plural = LANGUAGE_APP_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.contact.contact_title} - {self.language.name}'


class SocialNetwork(SortableMixin, Audit):
    name = models.CharField(
        verbose_name=SOCIAL_NAME,
        max_length=MAX_LENGTH_50
    )

    icon = models.ImageField(
        verbose_name=ICON,
        upload_to=PATH_LOGO_SOCIAL,
        null=True,
        blank=True
    )

    icon_css = models.CharField(
        verbose_name=ICON_CSS,
        max_length=MAX_LENGTH_50,
        null=True,
        blank=True
    )

    url = URLOrRelativeURLField(
        verbose_name=LINK_SOCIAL,
    )

    slug = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    order = models.PositiveIntegerField(
        verbose_name=ORDER,
        default=0
    )

    general_data = models.ForeignKey(
        'GeneralData',
        verbose_name=FOOTER,
        on_delete=models.SET_NULL,
        null=True
    )

    active = models.BooleanField(
        verbose_name=ACTIVE,
        default=True,
    )

    class Meta:
        ordering = ['order']
        verbose_name = SOCIAL_NETWORK_SING
        verbose_name_plural = SOCIAL_NETWORK_PLUR
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SocialNetwork, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.url})'


class GeneralData(Audit):
    title_one = models.CharField(
        verbose_name=TITLE,
        max_length=MAX_LENGTH_SHORT_TITLE,
        default='General Data'
    )

    logo_site = models.ImageField(
        verbose_name=LOGO,
        upload_to=PATH_LOGO_SITE,
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        verbose_name=ACTIVE,
        default=True,
    )

    slug_general_data = models.SlugField(
        verbose_name=SLUG,
        default=DEFAULT_VALUE
    )

    class Meta:
        ordering = ['-active', 'creation_date']
        verbose_name = GENERAL_DATA
        verbose_name_plural = GENERAL_DATA
        app_label = APP_LABEL

    def clean(self):
        actives = False
        this_is_active = self.active
        if this_is_active:
            actives = GeneralData.objects.filter(
                Q(active=True) & ~Q(id=self.id)
            )
        if actives:
            raise ValidationError({
                "active": ONE_GDATA_ACTIVE
            })

    def save(self, *args, **kwargs):
        self.slug_general_data = slugify(self.title_one)
        super(GeneralData, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_one


class PartnersGallery(SortableMixin, Audit):
    home = models.ForeignKey(
        GeneralData,
        verbose_name=GENERAL_DATA,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        verbose_name=IMAGE_INSTITUTION,
        upload_to=PATH_PARTNERS
    )

    url = models.URLField(
        verbose_name=URL_INSTITUTION,
        blank=True,
        null=True,
        default=None
    )

    order = models.SmallIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = PARTNERS_GALLERY
        verbose_name_plural = PARTNERS_GALLERY
        app_label = APP_LABEL

    def __str__(self):
        return f' {STR_PARTNER} {self.pk}'


class GeneralDataLanguage(LanguageAbstract):
    title_one = models.CharField(
        verbose_name=FOOTER_ONE,
        max_length=MAX_LENGTH_SHORT_TITLE,
        blank=True,
        null=True
    )

    about = RichTextField(
        verbose_name=FOOTER_ABOUT,
        blank=True,
        null=True,
        default=EMPTY_STRING
    )

    title_two = models.CharField(
        verbose_name=FOOTER_TWO,
        max_length=MAX_LENGTH_SHORT_TITLE,
        null=True,
        blank=True
    )

    general_data = models.ForeignKey(
        GeneralData,
        verbose_name=GENERAL_DATA,
        related_name=RELATED_NAME.format(GENERAL_DATA_LANG_KEY),
        on_delete=models.CASCADE,
        null=True
    )

    general_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'general_data'),)
        verbose_name = GENERAL_DATA_LANGUAGE
        verbose_name_plural = GENERAL_DATA_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return self.title_one
