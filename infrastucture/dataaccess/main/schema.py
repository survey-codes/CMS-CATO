import graphene

from infrastucture.dataaccess.contents.api.schema import PageQuery, GeneralInfoQuery
from infrastucture.dataaccess.tools.api.schema import LanguageQuery


class Query(GeneralInfoQuery, LanguageQuery, PageQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
