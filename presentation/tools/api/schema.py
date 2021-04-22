import graphene
from graphene_django import DjangoObjectType
from infrastructure.data_access.entities.tools import models


class LanguageType(DjangoObjectType):
    class Meta:
        model = models.Language
        fields = ("name", "abbreviation")


class LanguageQuery(graphene.ObjectType):
    languages = graphene.List(LanguageType)

    def resolve_languages(self, info, **kwargs):
        queryset = models.Language.objects.all()
        assert queryset.exists(), 'No hay lenguajes disponibles para el sitio'
        return queryset
