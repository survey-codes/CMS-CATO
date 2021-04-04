from django.db import transaction


def get_menu_as_dict(menu, lang):
    menu_data = {
        "menu": list()
    }
    items = menu.items.all()
    if items:
        for item in items:
            lang_item = item.item_lang.filter(language__abbreviation=lang.language.abbreviation).first()
            if lang_item is not None:
                menu_data["menu"].append(
                    lang_item.menu_item_metadata
                )

    return menu_data


def get_menu_item_as_dict(menu_item, lang):
    menu_item_data = {
        "name": lang.name,
    }

    if menu_item.url:
        menu_item_data["url"] = menu_item.url
        menu_item_data["external_url"] = True

    if menu_item.page_url:
        url = menu_item.page_url
        menu_item_data["url"] = url

    if menu_item.slug_url:
        menu_item_data["url"] = menu_item.slug_url

    children = menu_item.get_children()
    if children:
        menu_item_data["children"] = list()
        for child in children:
            children_menu = child.item_lang.filter(
                language__abbreviation=lang.language.abbreviation
            ).first()
            if children_menu is not None:
                menu_item_data["children"].append(
                    children_menu.menu_item_metadata
                )

        if len(menu_item_data["children"]) == 0:
            menu_item_data.pop("children")

    return menu_item_data

@transaction.atomic
def update_json_content_menu_item(menu_item, **kwargs):
    langs = menu_item.item_lang.select_related("language")
    for lang in langs:
        lang.menu_item_metadata = get_menu_item_as_dict(menu_item, lang)
        lang.save(update_fields=["menu_item_metadata"])


@transaction.atomic
def update_json_content_menu(menu, **kwargs):
    langs = menu.menu_lang.select_related("language")
    for lang in langs:
        lang.menu_metadata = get_menu_as_dict(menu, lang)
        lang.save(update_fields=["menu_metadata"])


