import graphene

from presentation.views.contents.general.general_query import GeneralQuery
from presentation.views.contents.page.page_query import PageQuery
from presentation.views.tools.language.language_query import LanguageQuery


class Query(LanguageQuery, GeneralQuery, PageQuery):
    pass


schema = graphene.Schema(query=Query)
