import graphene

from presentation.views.contents.general.general_query import GeneralQuery
from presentation.views.tools.language.language_query import LanguageQuery


class Query(LanguageQuery, GeneralQuery):
    pass


schema = graphene.Schema(query=Query)
