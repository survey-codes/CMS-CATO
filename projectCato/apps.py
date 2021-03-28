# my_project_app/apps.py
from django.contrib import admin
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem
from .settings import constants as c


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem(c.USER, icon='fa fa-user', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group'),
        ]),
        ParentItem(c.CONTENT, icon='fa fa-sitemap', children=[
            ChildItem(model='contents.menu'),
            ChildItem(model='contents.menuitem'),
            ChildItem(model='contents.page'),
            ChildItem(model='contents.generaldata'),
            ChildItem(model='contents.section'),
            ChildItem(model='contents.post'),
            ChildItem(model='contents.bannergallery'),
            ChildItem(model='contents.contact'),
        ]),
        ParentItem(c.SETTINGS, icon='fa fa-cogs', children=[
            ChildItem(model='tools.language'),
            ChildItem(model='contents.tag'),
            ChildItem(model='contents.sectiontemplate'),
            ChildItem(model='contents.postlanguage', label=c.IMPORT_EXPORT_LANGUAGE)

        ])

    )
# admin.site.site_header = 'PANEL DE ADMINISTRACIÓN GRUPO CATO'
