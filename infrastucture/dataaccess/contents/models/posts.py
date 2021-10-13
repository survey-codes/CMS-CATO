from adminsortable.models import SortableMixin
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from domain.utilities.content_tasks import post_update_jsonfield
from infrastucture.dataaccess.contents.constants import PATH_APP, MAX_LENGTH_50, MAX_LENGTH_URL, \
    DEFAULT_VALUE, APP_LABEL, MAX_LENGTH_SHORT_TITLE
from infrastucture.dataaccess.contents.models.sections import Section
from infrastucture.dataaccess.main.models.audit import Audit
from infrastucture.dataaccess.main.models.language_abstract import LanguageAbstract

CHOOSE_POSTS = _('Order posts')
IMAGE_360 = _("Is it a 360 image?")
IMAGE_HELP_TEXT = _('Check the box if is a 360 image')
LOAD_IMAGE = _('Load image')

PATH_POSTS = 'posts/'
PATH_POSTS_ICONS = f'{PATH_APP}{PATH_POSTS}icons'
PATH_POSTS_LOGOS = f'{PATH_APP}{PATH_POSTS}logos'
PATH_POSTS_GALLERIES = f'{PATH_APP}{PATH_POSTS}galleries'
PATH_POSTS_GALLERIES_PANORAMAS = f'{PATH_POSTS_GALLERIES}/panorama'

POST = _('Post')
POST_DESCRIPTION = _("Post description")
POST_GALLERY = _("Image")
POST_GALLERY_NAME = _('Post gallery name')
POST_GALLERY_PLURAL = _('Images')
POST_GALLERY_ERROR = _("You can't save an image and youtube video into the same gallery")
POST_ICON = _("Post icon")
POST_LINK = _('Post link')
POST_LOGO = _("Post logo")
POST_LANGUAGE = _('Post language')
POST_LANGUAGE_PLURAL = _('Post languages')
POST_PARENT = _("Post parent")
POST_PLURAL = _('Posts')
POST_SETTINGS = _('Post settings')
POST_SLUG = _('Post slug')
POST_TITLE = _("Post title")
POST_TRANSLATIONS = 'translations'

SHOW_FAMILY = _('Show family')
SHOW_FAMILY_HELP = _("Check the box if you want the post's family to shown in the section")

YOUTUBE_URL = _('Youtube video url')
YOUTUBE_URL_MAX_LENGTH = 255


class Post(MPTTModel, Audit):
    """

    """

    title = models.CharField(verbose_name=POST_TITLE, max_length=MAX_LENGTH_50, default='')
    logo = models.ImageField(verbose_name=POST_LOGO, upload_to=PATH_POSTS_LOGOS, blank=True)
    icon = models.ImageField(verbose_name=POST_ICON, upload_to=PATH_POSTS_ICONS, blank=True)
    parent = TreeForeignKey('self', verbose_name=POST_PARENT, on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(verbose_name=POST_LINK, max_length=MAX_LENGTH_URL, blank=True)
    slug = models.SlugField(verbose_name=POST_SLUG, default=DEFAULT_VALUE)
    sections = models.ManyToManyField(Section, through='PostSettings', related_name='posts')

    class Meta:
        verbose_name = POST
        verbose_name_plural = POST_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        self.update_translations()

    def update_translations(self):
        post_update_jsonfield.apply_async(kwargs={'post_id': self.pk}, countdown=5)


class PostGallery(SortableMixin, Audit):
    """

    """

    title = models.CharField(verbose_name=POST_GALLERY_NAME, max_length=MAX_LENGTH_SHORT_TITLE)
    image = models.ImageField(verbose_name=LOAD_IMAGE, upload_to=PATH_POSTS_GALLERIES_PANORAMAS, blank=True)
    is_360 = models.BooleanField(verbose_name=IMAGE_360, help_text=IMAGE_HELP_TEXT, default=False)
    youtube_url = models.CharField(verbose_name=YOUTUBE_URL, max_length=YOUTUBE_URL_MAX_LENGTH, blank=True)
    order = models.SmallIntegerField(default=0)
    post = models.ForeignKey(Post, verbose_name=POST, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order', ]
        verbose_name = POST_GALLERY
        verbose_name_plural = POST_GALLERY_PLURAL
        app_label = APP_LABEL

    def clean(self):
        if self.image and self.youtube_url:
            raise ValidationError(
                {
                    "image": POST_GALLERY_ERROR,
                }
            )

    def __str__(self):
        return f'{self.post}'


class PostLanguage(LanguageAbstract):
    """

    """

    title = models.CharField(verbose_name=POST_TITLE, max_length=MAX_LENGTH_50, default='')
    description = RichTextField(verbose_name=POST_DESCRIPTION, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name=POST_TRANSLATIONS)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)

    class Meta:
        unique_together = (('language', 'post'),)
        ordering = ['post', ]
        verbose_name = POST_LANGUAGE
        verbose_name_plural = POST_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.post}-{self.language}'


class PostSettings(models.Model):
    """

    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    show_family = models.BooleanField(verbose_name=SHOW_FAMILY, default=False, help_text=SHOW_FAMILY_HELP)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', ]
        verbose_name = POST_SETTINGS
        verbose_name_plural = CHOOSE_POSTS
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.section}'
