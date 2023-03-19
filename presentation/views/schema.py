from graphene import Schema

from presentation.views.contents.general.general_query import GeneralQuery
from presentation.views.contents.page.page_query import PageQuery
from presentation.views.tools.language.language_query import LanguageQuery
# from presentation.views.tools.user_pqrd_query import UserPqrdQuery


class Query(LanguageQuery, PageQuery, GeneralQuery):
    pass


schema = Schema(query=Query)
