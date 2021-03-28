import graphene
from contents.api.schema import PageQuery, GeneralInfoQuery
from tools.api.schema import LanguageQuery


class Query(GeneralInfoQuery, LanguageQuery, PageQuery, graphene.ObjectType):
    pass


# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
