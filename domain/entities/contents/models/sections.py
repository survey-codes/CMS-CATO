from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from domain.entities.contents.models.pages import Page
from domain.entities.contents.constants import APP_LABEL, DEFAULT_VALUE, MAX_LENGTH_20, MAX_LENGTH_50, MAX_LENGTH_SHORT_TITLE, PATH_APP
from domain.entities.main.models import Audit, LanguageAbstract


ALIGN_TEXTS = _('Posts texts alignment')
ALIGN_CHOICES = (
    ('RIGHT', _('Right')),
    ('LEFT', _('Left')),
    ('RIGHT_LEFT', _('Right - left')),
    ('LEFT_RIGHT', _('left - right'))
)
DEFAULT_ALIGN = "RIGHT"
DEFAULT_COLOR = "#FFFFFF"

PATH_SECTION = 'sections/'
PATH_SECTION_TEMPLATES = f'{PATH_APP}{PATH_SECTION}templates'
PATH_SECTION_BACKGROUND = f'{PATH_APP}{PATH_SECTION}backgrounds'

SECTION = _('Section')
SECTION_BACKGROUND_COLOR = _('Section background color')
SECTION_BACKGROUND_IMAGE = _('Section background image')
SECTION_DESCRIPTION = _('Section description')
SECTION_LANGUAGE = _('Section language')
SECTION_LANGUAGE_PLURAL = _('Section languages')
SECTION_PLURAL = _('Sections')
SECTION_SLUG = _('Section slug')
SECTION_TEMPLATE = _('Section template')
SECTION_TEMPLATE_PLURAL = _('Section templates')
SECTION_TITLE = _('Section title')
SECTION_TRANSLATIONS = 'translations'

SELECT_SECTION = _('Select section')
SELECT_SECTIONS = _('Select sections')

TEMPLATE_NAME = _('Template name')
TEMPLATE_NICKNAME = _('Template nickname')
TEMPLATE_PREVIEW = _('Template preview')


class SectionTemplate(models.Model):
    """

    """

    name = models.CharField(verbose_name=TEMPLATE_NAME, max_length=MAX_LENGTH_50)
    nickname = models.CharField(verbose_name=TEMPLATE_NICKNAME, max_length=MAX_LENGTH_20, blank=True)
    preview = models.ImageField(verbose_name=TEMPLATE_PREVIEW, upload_to=PATH_SECTION_TEMPLATES, blank=True)

    class Meta:
        verbose_name = SECTION_TEMPLATE
        verbose_name_plural = SECTION_TEMPLATE_PLURAL
        unique_together = (('name', 'nickname'),)
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.name}'


class Section(Audit):
    title = models.CharField(verbose_name=SECTION_TITLE, max_length=MAX_LENGTH_SHORT_TITLE, unique=True)
    background = models.ImageField(verbose_name=SECTION_BACKGROUND_IMAGE, upload_to=PATH_SECTION_BACKGROUND, null=True, blank=True)
    background_color = ColorField(verbose_name=SECTION_BACKGROUND_COLOR, default=DEFAULT_COLOR, null=True, blank=True)
    template = models.ForeignKey(SectionTemplate, verbose_name=SECTION_TEMPLATE, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name=SECTION_SLUG, default=DEFAULT_VALUE)
    order = models.PositiveSmallIntegerField(default=0)
    pages = models.ManyToManyField(Page, through='SectionSelector', related_name='sections')
    align = models.CharField(
        verbose_name=ALIGN_TEXTS,
        max_length=MAX_LENGTH_20,
        choices=ALIGN_CHOICES,
        default=DEFAULT_ALIGN
    )
    '''---------------------Visibility---------------------'''
    # title_visibility = models.BooleanField(
    #     verbose_name=TITLE_AS,
    #     default=True
    # )
    #
    # subtitle_visibility = models.BooleanField(
    #     verbose_name=SUBTITLE,
    #     default=False
    # )
    #
    # logo_visibility = models.PositiveSmallIntegerField(
    #     verbose_name=LOGO_VISIBILITY,
    #     choices=LOGO_IN,
    #     default=3,
    #     blank=False,
    #     null=False
    # )
    #
    # description_visibility = models.BooleanField(
    #     verbose_name=DESCRIPTION,
    #     default=False
    # )
    #
    # gallery_visibility = models.BooleanField(
    #     verbose_name=GALLERY_VISIBILITY,
    #     default=False
    # )
    '''----------------------------------------------------'''

    class Meta:
        ordering = ['order', ]
        verbose_name = SECTION
        verbose_name_plural = SECTION_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Section, self).save(*args, **kwargs)
        # Run background tasks on translations
        self.update_translations()

    def update_translations(self):
        section_update_jsonfield.apply_async(kwargs={'section_id': self.pk}, countdown=5)


class SectionLanguage(LanguageAbstract):
    """

    """

    title = models.CharField(verbose_name=SECTION_TITLE, max_length=MAX_LENGTH_SHORT_TITLE)
    description = RichTextField(verbose_name=SECTION_DESCRIPTION, null=True, blank=True)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name=SECTION_TRANSLATIONS)

    class Meta:
        unique_together = (('language', 'section'),)
        verbose_name = SECTION_LANGUAGE
        verbose_name_plural = SECTION_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(f'{self.section}-{self.language}')


class SectionSelector(Audit):
    """

    """

    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', ]
        verbose_name = SELECT_SECTION
        verbose_name_plural = SELECT_SECTIONS
        app_label = APP_LABEL

    def __str__(self):
        return f"{self.section}"
