import graphene
from graphene_django import DjangoObjectType
from domain.tools import models


class LanguageType(DjangoObjectType):
    class Meta:
        model = models.Language


class LanguageQuery(graphene.ObjectType):
    languages = graphene.List(LanguageType)

    def resolve_languages(self, info, **kwargs):
        qs = models.Language.objects.all()
        assert qs, 'No existen lenguajes'
        return qs
