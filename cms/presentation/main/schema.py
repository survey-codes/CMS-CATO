import graphene

from presentation.contents.api.schema import PageQuery, GeneralInfoQuery
from presentation.tools.api.schema import LanguageQuery


class Query(GeneralInfoQuery, LanguageQuery, PageQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
