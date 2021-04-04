from django.db import transaction


def get_banner_as_dict(banner, lang):
    banner_data = {
        "title": lang.title,
        "subtitle": lang.subtitle,
        "description": lang.banner_description,
        "background": "https://gqlcato.herokuapp.com{}".format(banner.image.url) if banner.image else None,
        "Type": None,
        "logo": "https://gqlcato.herokuapp.com{}".format(banner.animated_logo.url) if banner.animated_logo else None,
        "button_link": banner.button_link if banner.button_link else None,
        "icon_css": banner.icon_css_banner if banner.icon_css_banner else None,
        "video_url": banner.url_youtube if banner.url_youtube else None,
        "slug": banner.slug_banner,
    }

    return banner_data


def get_contact_as_dict(contact, lang):
    contact_data = {
        "title": contact.contact_title,
        "data": lang.about,
        "form": {
            "title": lang.title_form,
            "subtitle": lang.subtitle_form,
            "name": lang.name_form,
            "mail": lang.mail_form,
            "subject": {
                "title": lang.subject_form,
                "options": [
                    "Envíame un correo",
                    "Cotización",
                    "Alianza"
                ]
            },
            "body": lang.body_form,
            "text_button": lang.text_button,
        }
    }

    if contact.background:
        contact_data["background"] = "https://gqlcato.herokuapp.com{}".format(contact.background.url)

    return contact_data


def get_general_data_as_dict(general_data, lang):
    general_data_data = {
        "footer": lang.about,
    }

    if general_data.logo_site:
        general_data_data["logo"] = "https://gqlcato.herokuapp.com{}".format(general_data.logo_site.url)

    return general_data_data


def get_section_as_dict(section, lang):
    sect_data = {
        "title": lang.title,
        "description": lang.description,
        "background_image": "https://gqlcato.herokuapp.com{}".format(section.background.url) if section.background else None,
        "color": section.background_color,
        "component": section.component_type.component_name,
        "posts": list(),
        "slug": section.slug_section
    }

    settings = section.postsettings_set.select_related("post").all()
    if settings:
        for setting in settings:
            post = setting.post
            if post.active:
                try:
                    sect_data["posts"].insert(
                        setting.order - 1,
                        post.post_lang.get(
                            language__abbreviation=lang.language.abbreviation
                        ).post_metadata
                    )
                except Exception:
                    pass

    return sect_data


def get_post_as_dict(post, lang):
    post_data = {
        "title": lang.title_post,
        "subtitle": lang.subtitle,
        "description": lang.long_description,
        "image": "https://gqlcato.herokuapp.com{}".format(post.logo.url) if post.logo else None,
        "icon": "https://gqlcato.herokuapp.com{}".format(post.icon.url) if post.icon else None,
        "external_url": post.external_url if post.external_url else None,
        "tags": list(),
    }

    children = post.get_children()
    if children:
        post_data["extraposts"] = list()
        for child in children:
            if child.active:
                extrapost = child.post_lang.filter(
                    language__abbreviation=lang.language.abbreviation
                ).first()
                if extrapost is not None:
                    post_data["extraposts"].append(
                        extrapost.post_metadata
                    )

        if len(post_data["extraposts"]) == 0:
            post_data.pop("extraposts")

    tags = lang.tag.all()
    if tags:
        post_data["tags"] = list()
        for tag in tags:
            post_data["tags"].append(
                {
                    "name": tag.name,
                }
            )

    post_galleries = post.postgallery_set.all()
    if post_galleries:
        post_data["gallery"] = list()
        # image_indicator = False
        for gallery in post_galleries:
            if gallery.active:
                gallery_content = dict()
                gallery_content["title"] = gallery.title
                if gallery.image:
                    gallery_content["image"] = "https://gqlcato.herokuapp.com{}".format(gallery.image.url)
                    if gallery.image_360:
                        gallery_content["type"] = "img360"
                        # image_indicator = True
                    else:
                        gallery_content["type"] = "image"
                elif gallery.url_youtube:
                    gallery_content["video_url"] = gallery.url_youtube
                    gallery_content["type"] = "youtube"
                post_data["gallery"].append(gallery_content)
        if len(post_data.get("gallery")) > 1:
            post_data["type"] = "gallery"
        # else:
        #     gallery_instance = post_data.get("gallery")[0]
        #     if "image" in gallery_instance:
        #         post_data["type"] = "img360" if image_indicator else "image"
        #     if "video_url" in gallery_instance:
        #         post_data["type"] = "youtube"

    return post_data


def get_gallery_as_dict(gallery, lang):
    gallery_data = {
        "title": gallery.title,
        "slug": gallery.slug_banner_gallery,
        "active": gallery.active,
        "banners": list()
    }

    banners = gallery.banner_set.all().filter(
        banner_lang__language__abbreviation=lang.language.abbreviation
    )

    if banners:
        for banner in banners:
            if banner.active:
                gallery_data["banners"].append(
                    banner.banner_lang.get(
                        language__abbreviation=lang.language.abbreviation
                    ).banner_metadata
                )

    return gallery_data


def get_page_as_dict(page, lang):
    page_data = {
        "title": lang.title,
        "description": lang.description,
        "sections": list(),
    }

    if page.inner_menu:
        inner_menu_content = page.inner_menu.menu_lang.filter(
            language__abbreviation=lang.language.abbreviation
        ).first()
        if inner_menu_content:
            page_data["menu"] = inner_menu_content.menu_metadata.get("menu")

    selectors = page.sectionselector_set.select_related("section").all()
    if selectors:
        for selector in selectors:
            section = selector.section
            if section.active:
                try:
                    page_data["sections"].insert(
                        selector.order - 1,
                        section.section_lang.get(
                            language__abbreviation=lang.language.abbreviation
                        ).sect_metadata
                    )
                except Exception:
                    pass

    galleries = page.galleryselector_set.select_related("banner_gallery").all()
    if galleries:
        for gallery in galleries:
            if gallery.active:
                page_data["gallery"] = get_gallery_as_dict(
                    gallery.banner_gallery,
                    lang
                )

    return page_data


@transaction.atomic
def update_json_content_page(page, **kwargs):
    langs = page.page_lang.select_related("language")
    for lang in langs:
        lang.page_metadata = get_page_as_dict(page, lang)
        lang.save(update_fields=["page_metadata"])


@transaction.atomic
def update_json_content_section(section, **kwargs):
    langs = section.section_lang.select_related("language")
    for lang in langs:
        lang.sect_metadata = get_section_as_dict(section, lang)
        lang.save(update_fields=["sect_metadata"])


@transaction.atomic
def update_json_content_post(post, **kwargs):
    langs = post.post_lang.select_related("language")
    for lang in langs:
        lang.post_metadata = get_post_as_dict(post, lang)
        lang.save(update_fields=["post_metadata"])


@transaction.atomic
def update_json_content_banner(banner, **kwargs):
    langs = banner.banner_lang.select_related("language")
    for lang in langs:
        lang.banner_metadata = get_banner_as_dict(banner, lang)
        lang.save(update_fields=["banner_metadata"])


@transaction.atomic
def update_json_content_general_data(general_data, **kwargs):
    langs = general_data.general_data_lang.select_related("language")
    for lang in langs:
        lang.general_metadata = get_general_data_as_dict(general_data, lang)
        lang.save(update_fields=["general_metadata"])

@transaction.atomic
def update_json_content_contact(contact, **kwargs):
    langs = contact.contact_lang.select_related("language")
    for lang in langs:
        lang.contact_metadata = get_contact_as_dict(contact, lang)
        lang.save(update_fields=["contact_metadata"])
