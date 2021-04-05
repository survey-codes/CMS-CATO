from django.utils.translation import ugettext_lazy as _


JSON_UPDATE_MESSAGE = _('JSON content updated')

BANNERS_TITLE = _("Banner's title")
BANNERS_SUBTITLE = _("Banner's subtitle")
BANNERS_DESCRIPTION = _("Banner's description text")

EMPTY_FIELD = _("This field can't be empty")
IMAGE_NAME = _("Image name in spanish")
IMAGE_NAME_TRANSLATION = _("Image name in english")

LOAD_IMAGE = _('Load image')
IMAGE_360 = _("is it a 360 image?")
YOUTUBE_VIDEO = _("Youtube video url")
BANNER_LINK = _('Add link to banner')
BANNER_GALLERY = _("Banners gallery")
BANNER_GALLERY_PLURAL = _("Banners galleries")
BANNER_GALLERY_TITLE = _("Banner's gallery title")
GALLERY_SELECTOR = _("Select banners galleries")
IMAGE_DESCRIPTION = _('Description text')
PAGE_FK_BANNER_GALLERY = _('Show banner gallery in this page')
BACKGROUND_IMAGE = _('Background image')
JSON_CONTENT = _('Json content')

PAGE_TYPE_CHOICES = (
    ('MAKING', _('Construcción')),
    ('CONTENT', _('Contenido'))
)

PAGE_TYPE = _("Page's type")
PAGE_TITLE = _("Page's title")
PAGE_DESCRIPTION = _("Page's description")
PAGE_PARENT = _("Page's parent")
PAGE = _('Page')

POST_LANGUAGE = _('Post language')
POST_LANGUAGE_PLURAL = _('Post languages')

POST = _('Post')
POST_TITLE = _("Post's title")
POST_SUBTITLE = _("Post's subtitle")
POST_DESCRIPTION = _("Post's description text")
LOGO_POST = _("Post's image")
ICON_POST = _("Post's icon")
POST_PARENT = _("Post's parent")
TAG = _('Tags')
TAG_SINGULAR = _('Tag')
PAGE_SECTION = _("Page's section")

SELECT_SECTIONS = _('Select sections')
SECTION_TITLE = _("Section's title")
SECTION_DESCRIPTION = _("Section's description")
SECTION_BACKGROUND_COLOR = _("Section's background color")
ALIGN_TEXTS = _("Posts texts alignment")

ALIGN_CHOICES = (
    ('RIGHT', _('Right')),
    ('LEFT', _('Left')),
    ('RIGHT_LEFT', _('Right - left')),
    ('LEFT_RIGHT', _('left - right'))
)

COUNT_SECTIONS = _('Number of sections')
COUNT_IMAGES = _('Number of images in gallery')
USER = _('Registered users')
CONTENT = _('Content management')
SETTINGS = _('Tools')
COUNT_TRANSLATIONS = _('Number of translations')
IMPORT_EXPORT_LANGUAGE = _("Import-export data from post's language")
COMPONENT_TYPE = _("Section template")
VISIBILITY_HELP_TEXT = _('check the box if the posts component is visible in this section')

TITLE = _('Title')
SUBTITLE = _('Subtitle visibility')

LOGO = _('Logo')
DESCRIPTION = _('Description visibility')
LOGO_AS_TITLE = _('logo as title')
LOGO_PREVIEW = _('Logo(preview)')
IMAGE_HTML = '<img src="{}" style="-ms-interpolation-mode: bicubic;max-width:200px;max-height:auto;"/>'

SLIDER_VERTICAL = 'Slider vertical'

LOGO_IN = (
    (1, _('Above title')),
    (2, _('To the left of the title')),
    (3, _('To the left of the post')),
    (4, _('as background')),
    (5, _('No visible'))
)
LOGO_VISIBILITY_ERROR = _('You have to show the title to allocate the logo to the left of it')
LOGO_VISIBILITY = _('Image visibility')
TAGS_VISIBILITY = _('Tags visibility')

TITLE_AS = _('Title visibility')
EDIT_TEXT = _('Edit in another window')
CREATE_GALLERY = _('Create a gallery of banners')
BANNER_LANGUAGE_MODIFY = _("Edit banner's fields in language")
LANGUAGE_TAB = _('Language')
GALLERY = _('Gallery')
GALLERY_VISIBILITY = _('Gallery visibility')
VISIBILITY = _("post's visible fields")
POST_SETTINGS = _('Post settings')
POST_SETTINGS_PLURAL = _("Posts Settings")
GO_SECTION_LANGUAGE = _("Go to section's language")
SECTION_LANGUAGE_TEXT = _('Save and continue to section language')
CHOOSE_POSTS = _('Order posts')
GO_TO_POST_SETTINGS = _('(Save and continue to choose the posts for this section)')
SECTION_LANGUAGE = _("Edit fields in section's language")
SECTION = _('Section')
SECTION_PLURAL = _('Sections')
SECTION_POST = _("Section's posts")
IMAGE_HELP_TEXT = _('Check the box if is a 360 image')
POST_GALLERY = _("Image")
POST_GALLERY_PLURAL = _('Images')
POST_GALLERY_ERROR = _("You can't save an image and youtube video into the same gallery")
TEMPLATE_NAME = _('Template name')
TEMPLATE_NICKNAME = _('Template nickname')
TEMPLATE_TYPE_VB = _('Section template')
TEMPLATE_TYPE_PLURAL = _("Section templates")

CONTACT_INFORMATION = _('Contact Information')
CONTACT_LOCATION = _('Contact Location')
CONTACT_PAGE_TITLE = _('Contact page title')
BACKGROUND_FORM_IMAGE = _('Background form image')
CONTACT = _('Contact')
CONTACT_TITLE = _('Contact title')
CONTACT_PLURAL = _('Contacts')
CONTACT_ABOUT = _('Contact description')
TITLE_FORM_CONTACT = _('Title form contact')
SUBTITLE_FORM_CONTACT = _('Subtitle form contact')
NAME_FORM_CONTACT = _('Name form contact')
MAIL_FORM_CONTACT = _('Mail form contact')
AFFAIR_FORM_CONTACT = _('Affair form contact')
BODY_FORM_CONTACT = _('Body form contact')
TEXT_BUTTON_FORM_CONTACT = _('Text button form contact')

TAG_NAME = _('Tag name')
SECTION_LANGUAGE_SINGULAR = _("Section's language")
SECTION_LANGUAGE_PLURAL = _("Section's languages")

# -------CORE------------------#
ACTIVE = _('Active')
RELATED_NAME = '%(class)s_{}'

# --------TOOLS-----#
LANGUAGE_NAME = _('Language Name')
LANGUAGE_ABB = _('Language abbreviation')
LANGUAGE_APP_PLURAL = _('Languages')

SLUG = 'Slug'

FIELD_BANNER_LANGUAGE = _("Banner's language")
BANNER_LANGUAGE_PLURAL = _("Banner's laguages")
GO_BANNER_LANGUAGE = _('Go to Banner language tab')
BANNER_LANGUAGE_SAVE = _('Save and continue to edit banner language fields')

IMAGE_PREVIEW = _("Preview")

SOCIAL_NETWORK_SING = _('Social network')
SOCIAL_NETWORK_PLUR = _('Social networks')
ORDER = _('order')
LINK_SOCIAL = _('link social')
FOOTER = _('Footer')
SOCIAL_NAME = _('Social network name')
FOOTER_ONE = _('footer title one')
FOOTER_ABOUT = _('Footer description')
FOOTER_TWO = _('footer title two')
ICON = _('Icon')
ICON_PREVIEW = _('Icon (Preview)')
ICON_CSS = _('Icon css')

# ------------Banner-----------#
LOGO_ANIMATE = _('animated logo')
BUTTON_BANNER = _('text button banner')

ICON_LIST = _('List of icons')
ICON_LIST_URL = 'https://fontawesome.com/v4.7.0/icons/'
ICON_CSS_BUTTON_BANNER = _('icon css button banner')
GALLERY_MESSAGE_UNIQUE = _("The same gallery shouldn't be added more than once")
GALLERY_ERROR = _('Please select galleries that are active')

SHOW_FAMILY_HELP = _("Check the box if you want the post's family to shown in the section")
SHOW_FAMILY = _('Show family')
GENERAL_DATA = _("General data")
GENERAL_DATA_LANGUAGE = _("General data language")

GENERAL_DATA_LANGUAGE_PLURAL = _("General data languages")
GALLERIES = _('Galleries')
NO_POSTS = _("The section has no posts")
BANNER = _('Banner')
BANNER_PLURAL = _('Banners')

PATH_APP = 'Contents'
PATH_APP_TOOLS = 'Tools'
PATH_BANNER = f'{PATH_APP}/banners/'
PATH_ANIMATED_LOGO = f'{PATH_BANNER}/animated_logos'
PATH_ICON_POST = f'{PATH_BANNER}/icon_post'
PATH_CONTACT_BACKGROUND = f'{PATH_APP}/contacts/background'
PATH_SECTION_BACKGROUND = f'{PATH_APP}/sections/background'
PATH_IMAGES_GALLERIES = f'{PATH_APP}/Post_gallery_images'
PATH_LOGO_SITE = f'{PATH_APP_TOOLS}/logos'
PATH_LOGO_SOCIAL = f'{PATH_APP_TOOLS}/Logo_social'
PATH_PARTNERS = f'{PATH_APP}/partner_images'
PAGE_LANGUAGE = _('Page language')
PAGE_LANGUAGE_PLURAL = _('Page languages')
FIELD_MSG_GALLERY = _(
    "(choose a gallery, click on save and continue editing to see a preview of the first banner of it)")
IMAGE_INSTITUTION = _('Institution image')
URL_INSTITUTION = _("Institution url")
PARTNERS_GALLERY = _("Institutional links")
STR_PARTNER = _('partners link number ')
NO_PAGES = _("This section is not associated with any page")
NO_SECTIONS = _("This page does not contain sections")
SHOW_PAGES = _('Sections and pages in which appears ')
SHOW_PAGES_SECTION = _('Pages in which appears ')
ONE_GALLERY_ACTIVE = _('Only one banner gallery must be active')
ONE_FOOTER_ACTIVE = _('Only one general data must be active')
NO__POST_SECTIONS = _("This post is not contained in any section")
POST_PAGES = _("This post is not in a page")
ONE_GDATA_ACTIVE = _('Only one general data can be active')
RESTRICTION = _("Make sure this value is less or equal than 4 and greater or equal than 1")
LINES_VB = _("Display this many lines before show more")
QUANTITY_LINES = _("Between one and four lines")
PATH_BACKGROUND_POST = f'{PATH_APP}/Background_Thumnails'

# ------------Menu-----------#
MENU = _("Menu")
MENU_ITEM = _("Menu's item")
MENU_ITEM_LANGUAGE = _("Menu's item language")
