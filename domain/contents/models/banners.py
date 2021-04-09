# from django.db import models
#
# from domain.main.models import Audit
#
#
# class Banner(SortableMixin, Audit):
#     title = models.CharField(
#         verbose_name=BANNERS_TITLE,
#         max_length=MAX_LENGTH_TITLE
#     )
#
#     image = models.ImageField(
#         verbose_name=BACKGROUND_IMAGE,
#         upload_to=PATH_BANNER,
#         null=True,
#         blank=True
#     )
#
#     image_360 = models.BooleanField(
#         verbose_name=IMAGE_360,
#         help_text=IMAGE_HELP_TEXT,
#         default=False,
#         blank=True
#     )
#
#     animated_logo = models.ImageField(
#         verbose_name=LOGO_ANIMATE,
#         upload_to=PATH_ANIMATED_LOGO,
#         null=True,
#         blank=True
#     )
#
#     button_link = URLOrRelativeURLField(
#         verbose_name=BANNER_LINK,
#         blank=True,
#         null=True,
#         default=None
#     )
#
#     icon_css_banner = models.CharField(
#         verbose_name=ICON_CSS_BUTTON_BANNER,
#         max_length=MAX_LENGTH_20,
#         blank=True,
#         null=True,
#         default=None,
#         help_text=HELP_TEXT_ICON_CSS_BANNER
#     )
#
#     order = models.PositiveSmallIntegerField(
#         default=ORDER_VALUE_DEFAULT
#     )
#
#     url_youtube = models.CharField(
#         verbose_name=YOUTUBE_VIDEO,
#         max_length=MAX_LENGTH_URL_YOUTUBE,
#         blank=True,
#         null=True
#     )
#
#     banner_gallery = models.ForeignKey(
#         'BannerGallery',
#         verbose_name=BANNER_GALLERY,
#         on_delete=models.CASCADE,
#         null=True,
#     )
#
#     slug_banner = models.SlugField(
#         verbose_name=SLUG,
#         default=DEFAULT_VALUE
#     )
#
#     class Meta:
#         ordering = ['order', ]
#         verbose_name = BANNER
#         verbose_name_plural = BANNER_PLURAL
#         app_label = APP_LABEL
#
#     def save(self, *args, **kwargs):
#         self.slug_banner = slugify(self.title)
#         super(Banner, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return f"{self.title or N_N}"
#
#
# class BannerLanguage(LanguageAbstract):
#     title = models.CharField(
#         verbose_name=BANNERS_TITLE,
#         max_length=MAX_LENGTH_TITLE,
#         blank=True,
#         null=True
#     )
#
#     subtitle = models.CharField(
#         verbose_name=BANNERS_SUBTITLE,
#         max_length=MAX_LENGTH_TITLE,
#         blank=True,
#         null=True
#     )
#
#     banner_description = RichTextField(
#         verbose_name=BANNERS_DESCRIPTION,
#         blank=True,
#         null=True
#     )
#
#     button_text = models.CharField(
#         verbose_name=BUTTON_BANNER,
#         max_length=MAX_LENGTH_20,
#         blank=True,
#         null=True,
#         default=None
#     )
#
#     banner = models.ForeignKey(
#         'Banner',
#         verbose_name=BANNER,
#         on_delete=models.CASCADE,
#         related_name=RELATED_NAME.format(BANNER_LANG_KEY)
#     )
#
#     banner_metadata = JSONField(
#         blank=True,
#         null=True,
#         default=dict,
#         encoder=DjangoJSONEncoder
#     )
#
#     class Meta:
#         unique_together = (('language', 'banner'),)
#         verbose_name = FIELD_BANNER_LANGUAGE
#         verbose_name_plural = BANNER_LANGUAGE_PLURAL
#         app_label = APP_LABEL
#
#     def __str__(self):
#         return str(self.language)
#
#
# class BannerGallery(Audit):
#     title = models.CharField(
#         verbose_name=BANNER_GALLERY_TITLE,
#         max_length=MAX_LENGTH_TITLE,
#         null=False,
#         default=BANNER_GALLERY
#     )
#
#     slug_banner_gallery = models.SlugField(
#         verbose_name=SLUG,
#         default=DEFAULT_VALUE
#     )
#
#     def save(self, *args, **kwargs):
#         self.slug_banner_gallery = slugify(self.title)
#         super(BannerGallery, self).save(*args, **kwargs)
#
#     class Meta:
#         ordering = [f'-{CREATION_DATE_KEY}']
#         verbose_name = BANNER_GALLERY
#         verbose_name_plural = BANNER_GALLERY_PLURAL
#         app_label = APP_LABEL
#
#     def __str__(self):
#         return str(self.title)
#
#
# class GallerySelector(models.Model):
#     active = models.BooleanField(
#         verbose_name=ACTIVE,
#         default=False
#     )
#
#     page = models.ForeignKey(
#         'Page',
#         verbose_name=PAGE_FK_BANNER_GALLERY,
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL
#     )
#
#     banner_gallery = models.ForeignKey(
#         BannerGallery,
#         verbose_name=GALLERY_SELECTOR,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True
#     )
#
#     def clean(self):
#         # super(__class__, self).clean()
#         gallery = self.banner_gallery
#         if gallery:
#             if not gallery.active:
#                 raise ValidationError({
#                     "banner_gallery": GALLERY_ERROR
#                 })
#         else:
#             raise ValidationError({
#                 "banner_gallery": EMPTY_FIELD,
#             })
#
#     class Meta:
#         ordering = ['-active', ]
#         unique_together = (('page', 'banner_gallery'),)
#         verbose_name = BANNER_GALLERY
#         verbose_name_plural = BANNER_GALLERY_PLURAL
#         app_label = APP_LABEL
#
#     def unique_error_message(self, model_class, unique_check):
#         return GALLERY_MESSAGE_UNIQUE
#
#     def __str__(self):
#         return f"{self.page.title} gallery {self.id}"
