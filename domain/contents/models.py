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

from domain.menus.models import Menu
from presentation import constants as c
from domain.main.models import Audit, LanguageAbstract

APP_LABEL = "contents"

BANNERS_TITLE = _("Banner's title")
MAX_LENGTH_TITLE = 200
BACKGROUND_IMAGE = _('Background image')
PATH_BANNER = f'{c.PATH_APP}/banners/'
PATH_ANIMATED_LOGO = f'{PATH_BANNER}/animated_logos'
PATH_ICON_POST = f'{PATH_BANNER}/icon_post'
IMAGE_360 = _("is it a 360 image?")
IMAGE_HELP_TEXT = _('Check the box if is a 360 image')
LOGO_ANIMATE = _('animated logo')
BANNER_LINK = _('Add link to banner')
ICON_CSS_BUTTON_BANNER = _('icon css button banner')
MAX_LENGTH_ICON_CSS_BANNER = 20
ICON_LIST = _('List of icons')
ICON_LIST_URL = 'https://fontawesome.com/v4.7.0/icons/'
HELP_TEXT_ICON_CSS_BANNER = f"{ICON_LIST}: <a href={ICON_LIST_URL} target={'_blank'}> {ICON_LIST_URL} </a>"
ORDER_VALUE_DEFAULT = 0
YOUTUBE_VIDEO = _("Youtube video url")
MAX_LENGTH_URL_YOUTUBE = 255
BANNER_GALLERY = _("Banners gallery")


class Banner(SortableMixin, Audit):
    title = models.CharField(
        verbose_name=BANNERS_TITLE,
        max_length=MAX_LENGTH_TITLE
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
        max_length=MAX_LENGTH_ICON_CSS_BANNER,
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
        verbose_name=c.SLUG,
        default='-'
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = c.BANNER
        verbose_name_plural = c.BANNER_PLURAL
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_banner = slugify(self.title)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title or 'N/N'}"


class BannerLanguage(LanguageAbstract):
    title = models.CharField(
        verbose_name=BANNERS_TITLE,
        max_length=200,
        blank=True,
        null=True
    )

    subtitle = models.CharField(
        verbose_name=c.BANNERS_SUBTITLE,
        max_length=200,
        blank=True,
        null=True
    )

    banner_description = RichTextField(
        verbose_name=c.BANNERS_DESCRIPTION,
        blank=True,
        null=True
    )

    button_text = models.CharField(
        verbose_name=c.BUTTON_BANNER,
        max_length=20,
        blank=True,
        null=True,
        default=None
    )

    banner = models.ForeignKey(
        'Banner',
        verbose_name='banner',
        on_delete=models.CASCADE,
        related_name='banner_lang'
    )

    banner_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder
    )

    class Meta:
        unique_together = (('language', 'banner'),)
        verbose_name = c.FIELD_BANNER_LANGUAGE
        verbose_name_plural = c.BANNER_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.language)


class BannerGallery(Audit):
    title = models.CharField(
        c.BANNER_GALLERY_TITLE,
        max_length=200,
        null=False,
        default=BANNER_GALLERY
    )

    slug_banner_gallery = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    def save(self, *args, **kwargs):
        self.slug_banner_gallery = slugify(self.title)
        super(__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-creation_date']
        verbose_name = BANNER_GALLERY
        verbose_name_plural = c.BANNER_GALLERY_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.title)


class GallerySelector(models.Model):
    active = models.BooleanField(
        verbose_name=c.ACTIVE,
        default=False
    )

    page = models.ForeignKey(
        'Page',
        verbose_name=c.PAGE_FK_BANNER_GALLERY,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    banner_gallery = models.ForeignKey(
        BannerGallery,
        verbose_name=c.GALLERY_SELECTOR,
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
                    "banner_gallery": c.GALLERY_ERROR
                })
        else:
            raise ValidationError({
                "banner_gallery": c.EMPTY_FIELD,
            })

    class Meta:
        ordering = ['-active', ]
        unique_together = (('page', 'banner_gallery'),)
        verbose_name = BANNER_GALLERY
        verbose_name_plural = c.BANNER_GALLERY_PLURAL
        app_label = APP_LABEL

    def unique_error_message(self, model_class, unique_check):
        return c.GALLERY_MESSAGE_UNIQUE

    def __str__(self):
        return f"{self.page.title} gallery {self.id}"


class Page(MPTTModel, Audit):
    page_type = models.CharField(
        verbose_name=c.PAGE_TYPE,
        max_length=20,
        null=False,
        blank=False,
        choices=c.PAGE_TYPE_CHOICES,
        default='MAKING'
    )

    title = models.CharField(
        verbose_name=c.TITLE,
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )

    parent = TreeForeignKey(
        'self',
        verbose_name=c.PAGE_PARENT,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    inner_menu = models.ForeignKey(
        Menu,
        verbose_name=c.MENU,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    gallery_selector = models.ManyToManyField(
        'BannerGallery',
        verbose_name=c.GALLERY_SELECTOR,
        through='GallerySelector',
        blank=True,
    )

    order = models.PositiveSmallIntegerField(
        default=0,
    )

    slug_page = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    class Meta:
        verbose_name = c.PAGE
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_page = slugify(self.title)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class PageLanguage(LanguageAbstract):
    title = models.CharField(
        verbose_name=c.PAGE_TITLE,
        max_length=50
    )

    description = RichTextField(
        verbose_name=c.PAGE_DESCRIPTION,
        blank=True,
        null=True,
        default=''
    )

    page = models.ForeignKey(
        Page,
        verbose_name=c.PAGE,
        on_delete=models.CASCADE,
        related_name='page_lang'
    )

    page_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'page'),)
        verbose_name = c.PAGE_LANGUAGE
        verbose_name_plural = c.PAGE_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.language)


class Post(MPTTModel, Audit):
    title_post = models.CharField(
        verbose_name=c.POST_TITLE,
        max_length=50,
        blank=False,
        null=False
    )

    logo = models.ImageField(
        verbose_name=c.LOGO_POST,
        upload_to=PATH_ANIMATED_LOGO,
        blank=True
    )

    icon = models.ImageField(
        verbose_name=c.ICON_POST,
        upload_to=PATH_ICON_POST,
        blank=True
    )

    parent = TreeForeignKey(
        'self',
        verbose_name=c.POST_PARENT,
        null=True,
        on_delete=models.CASCADE,
        blank=True
    )

    external_url = models.URLField(
        verbose_name='URL externa',
        null=True,
        blank=True
    )

    slug_post = models.SlugField(
        default='-'
    )

    section = models.ManyToManyField(
        'Section',
        verbose_name=c.SECTION_PLURAL,
        through='PostSettings'
    )

    class Meta:
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_post = slugify(self.title_post)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title_post)


class PostLanguage(LanguageAbstract):
    title_post = models.CharField(
        verbose_name=c.POST_TITLE,
        max_length=50,
        blank=True,
        null=True
    )

    subtitle = models.CharField(
        verbose_name=c.POST_SUBTITLE,
        max_length=200,
        blank=True,
        null=True
    )

    long_description = RichTextField(
        verbose_name=c.POST_DESCRIPTION,
        blank=True,
        null=True
    )

    post = models.ForeignKey(
        Post,
        verbose_name=c.POST,
        on_delete=models.CASCADE,
        related_name='post_lang'
    )

    tag = models.ManyToManyField(
        'Tag',
        verbose_name=c.TAG,
        blank=True
    )

    post_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'post'),)
        ordering = ['post', ]
        verbose_name = c.POST_LANGUAGE
        verbose_name_plural = c.POST_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return '{} - {}'.format(
            self.post.title_post, self.language
        )


class SectionSelector(Audit):
    page = models.ForeignKey(
        'Page',
        verbose_name=c.PAGE_SECTION,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    section = models.ForeignKey(
        'Section',
        verbose_name=c.SECTION,
        on_delete=models.SET_NULL,
        null=True
    )

    order = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = c.SELECT_SECTIONS
        verbose_name_plural = c.SELECT_SECTIONS
        app_label = APP_LABEL

    def __str__(self):
        return f"{self.section}"


class Section(Audit):
    title = models.CharField(
        verbose_name=c.SECTION_TITLE,
        max_length=100,
        unique=True
    )

    page = models.ManyToManyField(
        'Page',
        verbose_name=c.PAGE_SECTION,
        blank=True,
        through='SectionSelector'
    )

    background = models.ImageField(
        verbose_name=BACKGROUND_IMAGE,
        upload_to=c.PATH_SECTION_BACKGROUND,
        blank=True,
        null=True
    )

    background_color = ColorField(
        verbose_name=c.SECTION_BACKGROUND_COLOR,
        default='#FFFFFF'
    )

    align = models.CharField(
        verbose_name=c.ALIGN_TEXTS,
        max_length=20,
        choices=c.ALIGN_CHOICES,
        default='RIGHT'
    )

    template = models.ForeignKey(
        'SectionTemplate',
        verbose_name=c.COMPONENT_TYPE,
        null=True,
        on_delete=models.CASCADE
    )

    slug_section = models.SlugField(
        default='-',
        verbose_name=c.SLUG
    )

    order = models.PositiveSmallIntegerField(
        default=0
    )

    lines_to_show = models.SmallIntegerField(
        default=1,
        verbose_name=c.LINES_VB,
        help_text=c.QUANTITY_LINES
    )

    '''---------------------Visibility---------------------'''
    title_visibility = models.BooleanField(
        verbose_name=c.TITLE_AS,
        default=True
    )

    subtitle_visibility = models.BooleanField(
        verbose_name=c.SUBTITLE,
        default=False
    )

    logo_visibility = models.PositiveSmallIntegerField(
        verbose_name=c.LOGO_VISIBILITY,
        choices=c.LOGO_IN,
        default=3,
        blank=False,
        null=False
    )

    tag_visibility = models.BooleanField(
        verbose_name=c.TAGS_VISIBILITY,
        default=False
    )

    description_visibility = models.BooleanField(
        verbose_name=c.DESCRIPTION,
        default=False
    )

    gallery_visibility = models.BooleanField(
        verbose_name=c.GALLERY_VISIBILITY,
        default=False
    )
    '''----------------------------------------------------'''

    class Meta:
        ordering = ['order', ]
        verbose_name = c.SECTION
        verbose_name_plural = c.SECTION_PLURAL
        app_label = APP_LABEL

    def clean(self):
        if self.logo_visibility == 2 and self.title_visibility is False:
            raise ValidationError({
                "title_visibility": c.LOGO_VISIBILITY_ERROR

            })
        if self.lines_to_show > 4 or self.lines_to_show < 1:
            raise ValidationError({
                "lines_to_show": c.RESTRICTION
            })

    def save(self, *args, **kwargs):
        self.slug_section = slugify(self.title)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class SectionLanguage(LanguageAbstract):
    title = models.CharField(
        verbose_name=c.SECTION_TITLE,
        max_length=100,
        blank=True,
        null=True
    )

    description = models.CharField(
        verbose_name=c.SECTION_DESCRIPTION,
        max_length=500,
        null=True,
        blank=True
    )

    section = models.ForeignKey(
        Section,
        verbose_name=c.SECTION,
        on_delete=models.CASCADE,
        related_name='section_lang'
    )

    sect_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'section'),)
        verbose_name = c.SECTION_LANGUAGE_SINGULAR
        verbose_name_plural = c.SECTION_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.language)


class Tag(models.Model):
    name = models.CharField(
        verbose_name=c.TAG_NAME,
        max_length=50
    )

    slug_tag = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    class Meta:
        verbose_name = c.TAG_SINGULAR
        verbose_name_plural = c.TAG
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_tag = slugify(self.name)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'#{self.name}'


class PostSettings(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name=c.SECTION_POST,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    section = models.ForeignKey(
        'Section',
        verbose_name=c.SECTION,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    show_family = models.BooleanField(
        verbose_name=c.SHOW_FAMILY,
        default=False,
        help_text=c.SHOW_FAMILY_HELP
    )

    order = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = c.POST_SETTINGS
        verbose_name_plural = c.CHOOSE_POSTS
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.section}'


class PostGallery(SortableMixin, Audit):
    active = models.BooleanField(
        verbose_name=c.ACTIVE,
        default=True
    )

    title = models.CharField(
        verbose_name=c.IMAGE_NAME,
        max_length=100,
        null=True
    )

    title_translation = models.CharField(
        verbose_name=c.IMAGE_NAME_TRANSLATION,
        max_length=100,
        null=True
    )

    image = models.ImageField(
        verbose_name=c.LOAD_IMAGE,
        upload_to=c.PATH_IMAGES_GALLERIES,
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
        max_length=255,
        blank=True,
        null=True
    )

    post = models.ForeignKey(
        Post,
        verbose_name=c.POST,
        on_delete=models.CASCADE
    )

    order = models.SmallIntegerField(
        default=0
    )

    slug_post_gallery = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    class Meta:
        ordering = ['order', ]
        verbose_name = c.POST_GALLERY
        verbose_name_plural = c.POST_GALLERY_PLURAL
        app_label = APP_LABEL

    def clean(self):
        if self.image and self.url_youtube:
            raise ValidationError(
                {
                    "image": c.POST_GALLERY_ERROR,
                }
            )
        pass

    def save(self, *args, **kwargs):
        self.slug_post_gallery = slugify(self.title)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.post}'


class SectionTemplate(models.Model):
    name = models.CharField(
        verbose_name=c.TEMPLATE_NAME,
        max_length=35
    )

    nickname = models.CharField(
        verbose_name=c.TEMPLATE_NICKNAME,
        max_length=35,
        null=True,
        blank=True
    )

    preview = models.ImageField(
        verbose_name=c.LOAD_IMAGE,
        upload_to=c.PATH_IMAGES_GALLERIES,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = c.TEMPLATE_NAME
        verbose_name_plural = c.TEMPLATE_TYPE_PLURAL
        unique_together = (('name', 'nickname'),)
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.name}'


class Contact(Audit):
    contact_title = models.CharField(
        verbose_name=c.CONTACT_TITLE,
        max_length=100,
        null=True,
        default=c.CONTACT
    )

    background = models.ImageField(
        verbose_name=c.BACKGROUND_FORM_IMAGE,
        upload_to=c.PATH_CONTACT_BACKGROUND,
        blank=True,
        null=True
    )

    slug_contact = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    class Meta:
        verbose_name = c.CONTACT
        verbose_name_plural = c.CONTACT_PLURAL
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug_contact = slugify(self.contact_title)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.contact_title}'


class ContactLanguage(LanguageAbstract):
    about = RichTextField(
        verbose_name=c.CONTACT_ABOUT,
        blank=True,
        null=True,
        default=''
    )

    contact = models.ForeignKey(
        Contact,
        verbose_name=c.CONTACT,
        related_name="contact_lang",
        on_delete=models.CASCADE,
    )

    title_form = models.CharField(
        verbose_name=c.TITLE_FORM_CONTACT,
        max_length=50,
        default=''
    )

    subtitle_form = models.CharField(
        verbose_name=c.SUBTITLE_FORM_CONTACT,
        max_length=50,
        default=''
    )

    name_form = models.CharField(
        verbose_name=c.NAME_FORM_CONTACT,
        max_length=50,
        default=''
    )

    mail_form = models.CharField(
        verbose_name=c.MAIL_FORM_CONTACT,
        max_length=50,
        default=''
    )

    subject_form = models.CharField(
        verbose_name=c.AFFAIR_FORM_CONTACT,
        max_length=50,
        default=''
    )

    body_form = models.TextField(
        verbose_name=c.BODY_FORM_CONTACT,
        default=''
    )

    text_button = models.CharField(
        verbose_name=c.TEXT_BUTTON_FORM_CONTACT,
        max_length=50,
        default=''
    )

    contact_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder
    )

    class Meta:
        unique_together = (('language', 'contact'),)
        verbose_name = c.LANGUAGE_TAB
        verbose_name_plural = c.LANGUAGE_APP_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return '{} - {}'.format(self.contact.contact_title, self.language.name)


class SocialNetwork(SortableMixin, Audit):
    name = models.CharField(
        verbose_name=c.SOCIAL_NAME,
        max_length=50
    )

    icon = models.ImageField(
        verbose_name=c.ICON,
        upload_to=c.PATH_LOGO_SOCIAL,
        null=True,
        blank=True
    )

    icon_css = models.CharField(
        verbose_name=c.ICON_CSS,
        max_length=50,
        null=True,
        blank=True
    )

    url = URLOrRelativeURLField(
        verbose_name=c.LINK_SOCIAL,
    )

    slug = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    order = models.PositiveIntegerField(
        verbose_name=c.ORDER,
        default=0
    )

    general_data = models.ForeignKey(
        'GeneralData',
        verbose_name=c.FOOTER,
        on_delete=models.SET_NULL,
        null=True
    )

    active = models.BooleanField(
        verbose_name=c.ACTIVE,
        default=True,
    )

    class Meta:
        ordering = ['order']
        verbose_name = c.SOCIAL_NETWORK_SING
        verbose_name_plural = c.SOCIAL_NETWORK_PLUR
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.url})'


class GeneralData(Audit):
    title_one = models.CharField(
        verbose_name=c.TITLE,
        max_length=100,
        default='General Data'
    )

    logo_site = models.ImageField(
        verbose_name=c.LOGO,
        upload_to=c.PATH_LOGO_SITE,
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        verbose_name=c.ACTIVE,
        default=True,
    )

    slug_general_data = models.SlugField(
        verbose_name=c.SLUG,
        default='-'
    )

    class Meta:
        ordering = ['-active', 'creation_date']
        verbose_name = c.GENERAL_DATA
        verbose_name_plural = c.GENERAL_DATA
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
                "active": c.ONE_GDATA_ACTIVE
            })

    def save(self, *args, **kwargs):
        self.slug_general_data = slugify(self.title_one)
        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_one


class PartnersGallery(SortableMixin, Audit):
    home = models.ForeignKey(
        GeneralData,
        verbose_name=c.GENERAL_DATA,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        verbose_name=c.IMAGE_INSTITUTION,
        upload_to=c.PATH_PARTNERS
    )

    url = models.URLField(
        verbose_name=c.URL_INSTITUTION,
        blank=True,
        null=True,
        default=None
    )

    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['order', ]
        verbose_name = c.PARTNERS_GALLERY
        verbose_name_plural = c.PARTNERS_GALLERY
        app_label = APP_LABEL

    def __str__(self):
        return f' {c.STR_PARTNER} {self.pk}'


class GeneralDataLanguage(LanguageAbstract):
    title_one = models.CharField(
        verbose_name=c.FOOTER_ONE,
        max_length=100,
        blank=True,
        null=True
    )

    about = RichTextField(
        verbose_name=c.FOOTER_ABOUT,
        blank=True,
        null=True,
        default=''
    )

    title_two = models.CharField(
        verbose_name=c.FOOTER_TWO,
        max_length=100,
        null=True,
        blank=True
    )

    general_data = models.ForeignKey(
        GeneralData,
        verbose_name=c.GENERAL_DATA,
        related_name="general_data_lang",
        on_delete=models.CASCADE,
        null=True
    )

    general_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        unique_together = (('language', 'general_data'),)
        verbose_name = c.GENERAL_DATA_LANGUAGE
        verbose_name_plural = c.GENERAL_DATA_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return self.title_one
