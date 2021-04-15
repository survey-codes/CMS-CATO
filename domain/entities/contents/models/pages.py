from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from domain.entities.contents.constants import APP_LABEL, DEFAULT_VALUE, MAX_LENGTH_20
from domain.entities.main.models import Audit, LanguageAbstract
from domain.entities.menus.models import Menu
from mptt.models import MPTTModel, TreeForeignKey


PAGE = _('Page')
PAGE_DESCRIPTION = _("Page description")
PAGE_LANGUAGE = _('Page language')
PAGE_LANGUAGE_PLURAL = _('Page languages')
PAGE_MENU = _('Page inner menu')
PAGE_PARENT = _("Page parent")
PAGE_PLURAL = _('Pages')
PAGE_SLUG = _('Page slug')
PAGE_TITLE = _('Page title')
PAGE_TRANSLATIONS = 'translations'


class Page(MPTTModel, Audit):
    """

    """

    title = models.CharField(verbose_name=PAGE_TITLE, max_length=MAX_LENGTH_20, unique=True)
    parent = TreeForeignKey('self', verbose_name=PAGE_PARENT, on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, verbose_name=PAGE_MENU, on_delete=models.CASCADE, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    slug = models.SlugField(verbose_name=PAGE_SLUG, default=DEFAULT_VALUE)

    class Meta:
        verbose_name = PAGE
        verbose_name_plural = PAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
        # Run background tasks on translations
        page_update_jsonfield.apply_async(kwargs={'page_id': self.pk}, countdown=10)


class PageLanguage(LanguageAbstract):
    """

    """

    title = models.CharField(verbose_name=PAGE_TITLE, max_length=MAX_LENGTH_20)
    description = RichTextField(verbose_name=PAGE_DESCRIPTION, null=True, blank=True)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name=PAGE_TRANSLATIONS)

    class Meta:
        unique_together = (('language', 'page'),)
        verbose_name = PAGE_LANGUAGE
        verbose_name_plural = PAGE_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(f'{self.page}-{self.language}')
