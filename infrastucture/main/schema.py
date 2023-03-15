import graphene

from infrastucture.contents.api.schema import PageQuery, GeneralInfoQuery
from infrastucture.tools import LanguageQuery


class Query(GeneralInfoQuery, LanguageQuery, PageQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
